from flask import Flask , render_template , redirect , request
from database import add_booking

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/about" , methods=["GET" , "POST"])
def about(): 
    return render_template("about.html")

@app.route("/service")
def service():
    return render_template("service.html")

@app.route("/customer" , methods=["GET" , "POST"])
def customer():
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        service = request.form.get("service")
        date = request.form.get("date")
        time = request.form.get("time")
        instructions = request.form.get("instructions")

        errors =[]
        if not name or len(name) < 3:
            errors.append("Name must be at least 3 characters..")

        if not phone or not phone.isdigit() or len(phone) != 10:
            errors.append("Enter a valid 10-digit phone number")

        if not service:
            errors.append("Please select a service")

        if not date:
            errors.append("Please select a date")

        if not time:
            errors.append("Please select a time slot.")

        if not instructions:
            instructions = "None"

        if errors:
            return render_template("customer.html" , errors = errors , form=request.form)

        
        else:
            add_booking(name , phone , service , date , time , instructions)

            print("details has been stored sucessfully in database")

            return render_template("success.html" , name= name , phone = phone , service = service , date = date , time = time, instructions =instructions )
        

    else:
        return render_template("customer.html")
    
@app.route("/contact" , methods = ["GET" , "POST"])
def contact():

    return render_template("contact.html")

@app.route('/contact_success')
def contact_success():
    return render_template("contact_success.html")

    
if __name__ == "__main__":
    app.run(debug=True)
