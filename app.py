from flask import Flask,render_template,request
import datetime
import pymongo


def create_app():
    app=Flask(__name__)
    db_client=pymongo.MongoClient("mongodb+srv://Kira:Ilovesh221b.@microblogflask.wm3rbil.mongodb.net/test")
    app.db=db_client.Microblog

    @app.route('/',methods=["GET","POST"])
    def home():
        if request.method=="POST":
            entry_content=request.form.get("content")
            formatted_date=datetime.datetime.today().strftime("%Y-%m-%d")
            time=datetime.datetime.today()
            # entries.append((entry_content,formatted_date))
            app.db.entries.insert_one({"content":entry_content,"date":formatted_date,"post time":time})
        entries=app.db.entries.find({}).sort("post time",pymongo.DESCENDING)
        return render_template('home.html',entries=entries)

    return app
