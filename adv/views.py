from django.shortcuts import redirect, render
from . models import content,Electronics,Contact
from django.contrib import messages


# Create your views here.
def home(request):
    best1 = content()
    best1.htag = "My CartPlus"
    best1.para = "A world of limitless possibilities awaits you - My CartPlus was kickstarted as a loyalty reward programme for all its regular customers at zero subscription fee. All you need is 500 supercoins to be a part of this service. For every 100 rupees spent on My Cartorder, Plus members earns 4 supercoins & non-plus members earn 2 supercoins."
    best1.img = 'mycartplus.jfif'


    best2 = content()
    best2.htag = "No Cost EMI"
    best2.para = "In an attempt to make high-end products accessible to all, our No Cost EMI plan enables you to shop with us under EMI, without shelling out any processing fee. Applicable on select mobiles, laptops, large and small appliances, furniture, electronics and watches, you can now shop without burning a hole in your pocket"
    best2.img = 'download.jfif'

    best3 = content()
    best3.htag = "EMI on Debit Cards"
    best3.para = "Did you know debit card holders account for 79.38 crore in the country, while there are only 3.14 crore credit card holders? After enabling EMI on Credit Cards, in another attempt to make online shopping accessible to everyone, My Cartintroduces EMI on Debit Cards, empowering you to shop confidently with us without having to worry about pauses in monthly cash flow."
    best3.img = 'emi.png'
    bestlist = [best1, best2, best3]


    whattitle = content()
    whattitle.htag = "What Can You Buy From My Cart?"
    whattitle.para = "Mobile Phones, Electronic Devices, Accessories Large Appliances and much more"

    what1 = content()
    what1.htag = "Mobile Phones"
    what1.para = "From budget phones to state-of-the-art smartphones, we have a mobile for everybody out there. Whether you're looking for larger, fuller screens, power-packed batteries, blazing-fast processors, beautification apps, high-tech selfie cameras or just large internal space, we take care of all the essentials."
    what1.img = 'mobile.jfif'

    what2 = content()
    what2.htag = "Electronic Devices and Accessories"
    what2.para = "When it comes to laptops, we are not far behind. Filter among dozens of super-fast operating systems, hard disk capacity, RAM, lifestyle, screen size and many other criterias for personalized results in a flash."
    what2.img = 'electronics.jfif'

    what3 = content()
    what3.htag = "Large Appliances"
    what3.para = "Sleek TVs, power-saving refrigerators, rapid-cooling ACs, resourceful washing machines - discover everything you need to run a house under one roof."
    what3.img = 'largeappliances.jfif'
    whatlist = [what1,what2,what3]

    banner1 = content()
    banner1.htag ="My Cart Cares \n - Creating Opportunities, Transforming Live"
    banner1.para = "At My Cart we believe the most radical and transformative of inventions are often those that empower others to unleash their creativity—to pursue their dreams. "
    banner1.img = 'store.jfif'
    title1 = content()
    title1.htag = "Building the future"
    title1.para = "We strive to have a positive impact on customers, employees, small businesses, the economy, and communities. My Cartians are smart, passionate builders with different backgrounds and goals, who share a common desire to always be learning and inventing on behalf of our customers."
    title1.img = 'teddy.jfif'

    displaycontact = True
    return render(request, 'index.html', {'bestlist': bestlist, 'whatlist': whatlist, 'banner1':banner1, 'title':title1, 'whattitle': whattitle, 'displaycontact':displaycontact })



def electronics(request):
    list = Electronics.objects.all()
    return render(request,'electronics.html',{'list':list })
#     toshiba = Electronics()
#     toshiba.img = 'toshiba.jfif'
#     toshiba.title = 'Toshiba'
#     toshiba.desc = 'toshiba is nice'
#     toshiba.offer = False

#     samsung = Electronics()
#     samsung.img = 'samsung.jfif'
#     samsung.title = 'Samsung'
#     samsung.desc = 'samsung is good'
#     samsung.offer = True
    
#     sony = Electronics()
#     sony.img = 'sony.jfif'
#     sony.title = 'Sony'
#     sony.desc = 'sony is wonderful'
#     sony.offer = True

#     list = [samsung, toshiba, sony]
#     return render(request, 'electronics.html', {'list':list})

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['message']
        user = request.user
        print(request.user)
        contact = Contact(name=name, email=email, phone=phone, msg=msg)
        contact.save()
        print('contact saved')
        messages.success(request, f'Message successfully submitted by user - {user}')
        return redirect('/')


    