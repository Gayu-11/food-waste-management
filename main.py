from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import mysql.connector
import os
import datetime
from geopy.distance import geodesic
import numpy as np
import folium
from sklearn.cluster import OPTICS
from sklearn.preprocessing import StandardScaler

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'abcdef'

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    charset="utf8",
    database="food_waste"
)

@app.route('/',methods=['POST','GET'])
def index():

    
    return render_template('index.html')

@app.route('/provider_log',methods=['POST','GET'])
def provider_log():

    msg=""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM fo_provider WHERE username = %s AND password = %s AND action = 1', (username, password))
        account = cursor.fetchone()
        
        if account:
            session['username'] = username
            session['user_type'] = 'provider'
            msg="success"  
        else:
            msg="fail"

    
    return render_template('provider_log.html', msg=msg)




@app.route('/provider_reg',methods=['POST','GET'])
def provider_reg():
    
    msg=""
    if request.method=='POST':
        place=request.form['place']
        name=request.form['name']
        address=request.form['address']
        city=request.form['city']
        mobile=request.form['mobile']
        email=request.form['email']
        username=request.form['username']
        password=request.form['password']
        longitude=request.form['longitude']
        latitude=request.form['latitude']
        now = datetime.datetime.now()
        reg_date=now.strftime("%Y-%m-%d")
        
        mycursor = mydb.cursor()
        mycursor.execute("SELECT count(*) FROM fo_provider where username=%s",(username, ))
        cnt = mycursor.fetchone()[0]
        if cnt==0:
            mycursor.execute("SELECT max(id)+1 FROM fo_provider")
            maxid = mycursor.fetchone()[0]
            if maxid is None:
                maxid=1
            sql = "INSERT INTO fo_provider(id, place, name, address, mobile, email, username, password, reg_date, longitude, latitude, city) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (maxid, place, name, address, mobile, email, username, password, reg_date, longitude, latitude, city)
            mycursor.execute(sql, val)
            mydb.commit()

            msg="success"
        else:
            msg="fail"
  
    return render_template('provider_reg.html', msg=msg)


@app.route('/user_log',methods=['POST','GET'])
def user_log():

    msg=""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM fo_user WHERE username = %s AND password = %s AND action = 1', (username, password))
        account = cursor.fetchone()
        
        if account:
            session['username'] = username
            session['user_type'] = 'user'
            msg="success"  
        else:
            msg="fail"

    
    return render_template('user_log.html', msg=msg)



@app.route('/user_reg',methods=['POST','GET'])
def user_reg():
    
    msg=""
    if request.method=='POST':
        org_name=request.form['org_name']
        name=request.form['name']
        address=request.form['address']
        city=request.form['city']
        mobile=request.form['mobile']
        email=request.form['email']
        username=request.form['username']
        password=request.form['password']
        longitude=request.form['longitude']
        latitude=request.form['latitude']
        now = datetime.datetime.now()
        reg_date=now.strftime("%Y-%m-%d")
        
        mycursor = mydb.cursor()
        mycursor.execute("SELECT count(*) FROM fo_user where username=%s",(username, ))
        cnt = mycursor.fetchone()[0]
        if cnt==0:
            mycursor.execute("SELECT max(id)+1 FROM fo_user")
            maxid = mycursor.fetchone()[0]
            if maxid is None:
                maxid=1
            sql = "INSERT INTO fo_user(id, org_name, name, address, mobile, email, username, password, reg_date, longitude, latitude, city) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (maxid, org_name, name, address, mobile, email, username, password, reg_date, longitude, latitude, city)
            mycursor.execute(sql, val)
            mydb.commit()

            msg="success"
        else:
            msg="fail"
  
    return render_template('user_reg.html', msg=msg)

@app.route('/user_home', methods=['POST', 'GET'])
def user_home():
    if 'username' not in session or session.get('user_type') != 'user':
        print("Please log in as a admin to access the page.", 'danger')
        return redirect(url_for('user_log'))
    
    cursor = mydb.cursor()
    username = session.get('username')
    cursor.execute("SELECT * FROM fo_user WHERE username = %s", (username,))
    data = cursor.fetchone()
    cursor.close()

    return render_template('user_home.html', data=data)

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method=='POST':
        id_data=request.form['id']
        address=request.form['address']
        mobile=request.form['mobile']
        email=request.form['email']

        cursor=mydb.cursor()
        cursor.execute(" UPDATE fo_user SET address=%s, mobile=%s, email=%s where id = %s", (address, mobile, email, id_data))
        print("Data Updated Successfully")
        mydb.commit()
    
    return redirect('user_home')


@app.route('/provider_home', methods=['POST', 'GET'])
def provider_home():
    if 'username' not in session or session.get('user_type') != 'provider':
        print("Please log in as a admin to access the page.", 'danger')
        return redirect(url_for('provider_log'))
    
    cursor = mydb.cursor()
    username = session.get('username')
    cursor.execute("SELECT * FROM fo_provider WHERE username = %s", (username,))
    data = cursor.fetchone()
    cursor.close()

    return render_template('provider_home.html', data=data)

@app.route('/update1', methods=['GET', 'POST'])
def update1():
    if request.method=='POST':
        id_data=request.form['id']
        address=request.form['address']
        mobile=request.form['mobile']
        email=request.form['email']

        cursor=mydb.cursor()
        cursor.execute(" UPDATE fo_provider SET address=%s, mobile=%s, email=%s where id = %s", (address, mobile, email, id_data))
        print("Data Updated Successfully")
        mydb.commit()
    
    return redirect('provider_home')

@app.route('/food_post', methods=['POST', 'GET'])
def food_post():
    if 'username' not in session or session.get('user_type') != 'provider':
        print("Please log in as a admin to access the page.", 'danger')
        return redirect(url_for('provider_log'))
    
    dt=""
    food_type=None
    post_id=None
    username = session.get('username')
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM fo_provider WHERE username = %s", (username,))
    data = cursor.fetchall()
    cursor.close()

    
    
    msg=""
    nearby_users = []
    num_nearby_users = 0
    provider_coords = None  # Initialize with a default value
    if request.method=='POST':
        food_type=request.form['food_type']
        quantity=request.form['quantity']
        message=request.form['message']
        place=request.form['place']
        name=request.form['name']
        address=request.form['address']
        city=request.form['city']
        mobile=request.form['mobile']
        longitude=request.form['longitude']
        latitude=request.form['latitude']
        now = datetime.datetime.now()
        post_date=now.strftime("%B %d, %Y")
        post_time=now.strftime("%I:%M %p")
        
        mycursor = mydb.cursor()
        
        mycursor.execute("SELECT max(id)+1 FROM fo_post")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid=1
        sql = "INSERT INTO fo_post(id, food_type, quantity, message, place, name, address, mobile, post_date, post_time, username, city, longitude, latitude) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (maxid, food_type, quantity, message, place, name, address, mobile, post_date, post_time, username, city, longitude, latitude)
        mycursor.execute(sql, val)
        mydb.commit()

        msg="success"

        

        try:
            provider_cursor = mydb.cursor(dictionary=True)
            provider_cursor.execute("SELECT * FROM fo_provider WHERE username = %s", (username,))
            provider_data = provider_cursor.fetchone()
            provider_cursor.close()

            # Extract provider coordinates
           
            provider_coords = (provider_data['latitude'], provider_data['longitude'])

            print("Provider Coordinates:", provider_coords)

            # Fetch all users with valid latitude and longitude
            user_cursor = mydb.cursor(dictionary=True)
            user_cursor.execute("SELECT username, latitude, longitude FROM fo_user WHERE latitude IS NOT NULL AND longitude IS NOT NULL")
            all_users = user_cursor.fetchall()
            user_cursor.close()

            for user in all_users:
                user_coords = (user['latitude'], user['longitude'])
                distance = geodesic(provider_coords, user_coords).kilometers


                if distance < 50:  # Adjust the distance threshold as needed
                    user_details = get_user_details(user['username'])  # Fetch additional details
                    if user_details:
                        nearby_users.append({
                            'username': user['username'],
                            'latitude': user['latitude'],
                            'longitude': user['longitude'],
                            'user_details': user_details 
                        }) 

            # Count the number of nearby users
            num_nearby_users = len(nearby_users)

        except Exception as e:
            print(f"An error occurred: {e}")
    

    return render_template('food_post.html', fo_provider=data, msg=msg, nearby_users=nearby_users, num_nearby_users=num_nearby_users, provider_coords=provider_coords, username=username, fo_food=dt, food_type=food_type, post_id=post_id)
    
def get_user_details(username):
    try:
        user_cursor = mydb.cursor(dictionary=True)
        user_cursor.execute("SELECT * FROM fo_user WHERE username = %s", (username,))
        user_details = user_cursor.fetchone()
        user_cursor.close()
        return user_details
    except Exception as e:
        print(f"An error occurred while fetching user details: {e}")
        return None

@app.route('/food_item', methods=['GET', 'POST'])
def food_item():
    if request.method=='POST':
        id_data=request.form['post_id']
        selected_food_items = request.form.getlist('food_items[]')

        cursor = mydb.cursor()

        # Update the fo_post table with the selected food items
        # Assuming you have a column named 'food_items' in the fo_post table
        cursor.execute("UPDATE fo_post SET food_item = %s WHERE id = %s", (','.join(selected_food_items), id_data))
        mydb.commit()
        cursor.close()
    
    return redirect('food_post')


@app.route('/view_post', methods=['POST', 'GET'])
def view_post():
    if 'username' not in session or session.get('user_type') != 'user':
        print("Please log in as a admin to access the page.", 'danger')
        return redirect(url_for('user_log'))

    
    username = session.get('username')

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM fo_user where username = %s", (username,))
    data2 = cursor.fetchone()
    cursor.close()

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM fo_post")
    pos = cursor.fetchall()
    cursor.close()



    valid_posts = []
    try:
        cursor = mydb.cursor(dictionary=True)
        cursor.execute("SELECT latitude, longitude FROM fo_user WHERE username = %s", (username,))
        user_location = cursor.fetchone()
        cursor.close()
        

        user_coords = (user_location['latitude'], user_location['longitude'])
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM fo_post WHERE longitude IS NOT NULL AND latitude IS NOT NULL")
        posts = cursor.fetchall()

        # Filter posts based on distance
        valid_posts = []
        for post in posts:
            post_coords = (post['latitude'], post['longitude'])
            distance = geodesic(user_coords, post_coords).kilometers
            if distance < 100:  # Change the distance threshold as needed
                valid_posts.append(post)

        cursor.close()
                    
        
           

    except Exception as e:
        print(f"An error occurred: {e}")



    
        

    msg=""
    if request.method=='POST':
        user_name=request.form['user_name']
        user_mobile=request.form['user_mobile']
        user_email=request.form['user_email']
        user_address=request.form['user_address']
        pro_place=request.form['pro_place']
        pro_address=request.form['pro_address']
        food_type=request.form['food_type']
        quantity=request.form['quantity']
        pro_username=request.form['pro_username']
        pro_mobile=request.form['pro_mobile']
        post_date=request.form['post_date']
        post_time=request.form['post_time']
        post_id=request.form['post_id']
        now = datetime.datetime.now()
        formatted_date = now.strftime("%B %d, %Y")
        
        mycursor = mydb.cursor()
        
        mycursor.execute("SELECT max(id)+1 FROM fo_booking")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid=1
        sql = "INSERT INTO fo_booking(id, user_name, user_mobile, user_email, user_address, pro_place, pro_address, food_type, quantity, pro_username, pro_mobile, post_date, post_time, post_id, username, book_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
        val = (maxid, user_name, user_mobile, user_email, user_address, pro_place, pro_address, food_type, quantity, pro_username, pro_mobile, post_date, post_time, post_id, username, formatted_date)
        mycursor.execute(sql, val)
        mydb.commit()

        msg="success"

        cursor = mydb.cursor()
        cursor.execute("DELETE FROM fo_post WHERE id = %s", (post_id,))
        mydb.commit()
        cursor.close()

    
    

    return render_template('view_post.html', data2=data2, msg=msg, posts=valid_posts, fo_post=pos)

@app.route('/book_req', methods=['GET', 'POST'])
def book_req():
    if 'username' not in session or session.get('user_type') != 'user':
        print("Please log in as a admin to access the page.", 'danger')
        return redirect(url_for('user_log'))

    
    username=session.get('username')

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM fo_booking where username = %s",(username,))
    data3 = cursor.fetchall()
    cursor.close()
   
   
    return render_template('book_req.html', fo_booking=data3)

@app.route('/view_req', methods=['POST', 'GET'])
def view_req():
    if 'username' not in session or session.get('user_type') != 'provider':
        print("Please log in as a admin to access the page.", 'danger')
        return redirect(url_for('provider_log'))

    username=session.get('username')
    
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM fo_booking where pro_username = %s", (username,))
    data = cursor.fetchall()
    cursor.close()


    now = datetime.datetime.now()
    current_datetime = now.strftime("%B %d, %Y")

    # Connect to MySQL and delete posts with post_date in the past
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM fo_post WHERE post_date < %s", (current_datetime,))
    mydb.commit()
    cursor.close()

    
    
    mobile=""
    email=""
    name=""
    st=""
    mess=""
    aid=""
    act=request.args.get("act")

    if act=="ok":
        aid=request.args.get("aid")
        cursor = mydb.cursor()
        cursor.execute("update fo_booking set action=1 where id=%s",(aid,))
        mydb.commit()
        st="1"
        aid=request.args.get("aid")
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM fo_booking where id = %s", (aid,))
        data1 = cursor.fetchone()
        if data1 is not None:
            mobile = data1[2]
            email = data1[3]
            name = data1[1]
            mess = f"Reminder: Hi {data1[1], data1[5]} has accepted your request!"
        

        
        
    if act=="no":
        aid=request.args.get("aid")
        cursor = mydb.cursor()
        cursor.execute("update fo_booking set action=2 where id=%s",(aid,))
        mydb.commit()
        print("your account will be rejected")


    return render_template('view_req.html', fo_booking=data, mobile=mobile, email=email, name=name, mess=mess, st=st)





@app.route('/send_post', methods=['POST', 'GET'])
def send_post():
    if 'username' not in session or session.get('user_type') != 'user':
        print("Please log in as a admin to access the page.", 'danger')
        return redirect(url_for('user_log'))

    username=session.get('username')

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM fo_user where username = %s",(username,))
    data2 = cursor.fetchone()
    cursor.close()
    

    msg=""
    if request.method=='POST':
        user_name=request.form['user_name']
        user_mobile=request.form['user_mobile']
        user_email=request.form['user_email']
        user_address=request.form['user_address']
        food_type=request.form['food_type']
        quantity=request.form['quantity']
        now = datetime.datetime.now()
        formatted_date = now.strftime("%B %d, %Y")
        
        mycursor = mydb.cursor()
        
        mycursor.execute("SELECT max(id)+1 FROM fo_need")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid=1
        sql = "INSERT INTO fo_need(id, user_name, user_mobile, user_email, user_address, food_type, quantity, post_date, username) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (maxid, user_name, user_mobile, user_email, user_address, food_type, quantity, formatted_date, username)
        mycursor.execute(sql, val)
        mydb.commit()

        msg="success"

    return render_template('send_post.html', data2=data2, msg=msg)


@app.route('/need_post', methods=['POST', 'GET'])
def need_post():
    if 'username' not in session or session.get('user_type') != 'provider':
        print("Please log in as a admin to access the page.", 'danger')
        return redirect(url_for('provider_log'))

    username=session.get('username')
    
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM fo_need")
    data = cursor.fetchall()
    cursor.close()

    
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM fo_provider where username = %s",(username,))
    data2 = cursor.fetchone()
    cursor.close()

    msg=""
    user_mobile=""
    user_name=""
    user_email=""
    mess=""
    st=""
    if request.method=='POST':
        av_time=request.form['av_time']
        user_name=request.form['user_name']
        username1=request.form['username1']
        user_mobile=request.form['user_mobile']
        user_email=request.form['user_email']
        user_address=request.form['user_address']
        food_type=request.form['food_type']
        quantity=request.form['quantity']
        pro_place=request.form['pro_place']
        pro_address=request.form['pro_address']
        pro_name=request.form['pro_name']
        pro_mobile=request.form['pro_mobile']
        now = datetime.datetime.now()
        donate_date = now.strftime("%B %d, %Y")
        
        mycursor = mydb.cursor()
        
        mycursor.execute("SELECT max(id)+1 FROM fo_donate")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid=1
        sql = "INSERT INTO fo_donate(id, user_name, username1, user_mobile, user_address, food_type, quantity, username , pro_place, pro_address, pro_name, pro_mobile, donate_date, user_email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s,%s)"
        val = (maxid, user_name, username1, user_mobile, user_address, food_type, quantity, username , pro_place, pro_address, pro_name, pro_mobile, donate_date, user_email)
        mycursor.execute(sql, val)
        mydb.commit()

        # Delete the post from fo_need table
        delete_id = request.form['delete_id']  # Make sure you have a hidden input in your form with name="delete_id" containing the post ID to delete
        mycursor.execute("DELETE FROM fo_need WHERE id = %s", (delete_id,))
        mydb.commit()

        msg="success"
        st="1"
        mess = f"Reminder: Hi {user_name}, {pro_name} has ready to donate!"

        mycursor.close()
        

    return render_template('need_post.html', fo_need=data, data2=data2, msg=msg, user_mobile=user_mobile, user_email=user_email, user_name=user_name, mess=mess, st=st)


@app.route('/view_volun', methods=['POST', 'GET'])
def view_volun():
    
    if 'username' not in session or session.get('user_type') != 'user':
        print("Please log in as a admin to access the page.", 'danger')
        return redirect(url_for('user_log'))

    username=session.get('username')
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM fo_donate where username1 = %s",(username,))
    data2 = cursor.fetchall()
    cursor.close()

    return render_template('view_volun.html', fo_donate=data2)


@app.route('/admin_log',methods=['POST','GET'])
def admin_log():

    msg=""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM fo_admin WHERE username = %s AND password = %s', (username, password))
        account = cursor.fetchone()
        
        if account:
            session['username'] = username
            session['user_type'] = 'admin'
            msg="success"  
        else:
            msg="fail"

    
    return render_template('admin_log.html', msg=msg)

@app.route('/admin_access', methods=['POST', 'GET'])
def admin_access():
    
    if 'username' not in session or session.get('user_type') != 'admin':
        print("Please log in as a admin to access the page.", 'danger')
        return redirect(url_for('admin_log'))

    
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM fo_user")
    data1 = cursor.fetchall()
    cursor.close()

    act=request.args.get("act")

    if act=="ok":
        aid=request.args.get("aid")
        cursor = mydb.cursor()
        cursor.execute("update fo_user set action=1 where id=%s",(aid,))
        mydb.commit()
        print("successfully accepted")
        
    if act=="no":
        aid=request.args.get("aid")
        cursor = mydb.cursor()
        cursor.execute("update fo_user set action=2 where id=%s",(aid,))
        mydb.commit()
        print("your account will be rejected")

    return render_template('admin_access.html', fo_user=data1)

@app.route('/admin_access2', methods=['POST', 'GET'])
def admin_access2():
    
    if 'username' not in session or session.get('user_type') != 'admin':
        print("Please log in as a admin to access the page.", 'danger')
        return redirect(url_for('admin_log'))

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM fo_provider")
    data1 = cursor.fetchall()
    cursor.close()

    act=request.args.get("act")

    if act=="ok":
        aid=request.args.get("aid")
        cursor = mydb.cursor()
        cursor.execute("update fo_provider set action=1 where id=%s",(aid,))
        mydb.commit()
        print("successfully accepted")
        
    if act=="no":
        aid=request.args.get("aid")
        cursor = mydb.cursor()
        cursor.execute("update fo_provider set action=2 where id=%s",(aid,))
        mydb.commit()
        print("your account will be rejected")
    

    return render_template('admin_access2.html', fo_provider=data1)


@app.route('/add_food', methods=['POST', 'GET'])
def add_food():

    msg=""
    if request.method=='POST':

        food_type=request.form['food_type']
        food_item=request.form['food_item']
        
        
        mycursor = mydb.cursor()
        mycursor.execute("SELECT max(id)+1 FROM fo_food")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid=1
        sql = "INSERT INTO fo_food(id, food_type, food_item) VALUES (%s, %s, %s)"
        val = (maxid, food_type, food_item)
        mycursor.execute(sql, val)
        mydb.commit()

        msg="success"

    return render_template('add_food.html', msg=msg)



@app.route('/book_report', methods=['POST', 'GET'])
def book_report():
    
    if 'username' not in session or session.get('user_type') != 'admin':
        print("Please log in as a admin to access the page.", 'danger')
        return redirect(url_for('admin_log'))

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM fo_booking")
    data1 = cursor.fetchall()
    cursor.close()

    return render_template('book_report.html', fo_booking=data1)


@app.route('/report', methods=['POST', 'GET'])
def report():
    
    if 'username' not in session or session.get('user_type') != 'admin':
        print("Please log in as a admin to access the page.", 'danger')
        return redirect(url_for('admin_log'))

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM fo_donate")
    data1 = cursor.fetchall()
    cursor.close()

    return render_template('report.html', fo_donate=data1)

@app.route('/logout')
def logout():
    
    session.clear()
    print("Logged out successfully", 'success')
    return redirect(url_for('index'))



if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=5000)
