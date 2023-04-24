from app.models import ContactRequest


def GetContactList():
    return [
        ["Berk", "Satış", "Yüksek"],
        ["Ezgi", "İK", "Orta"],
        ["Ali", "Nakliye", "Düşük"]
    ]




def SaveContactRequest(name, email, category, priority, message):
    contactRequest = ContactRequest()
    contactRequest.name = name
    contactRequest.email = email
    contactRequest.category = category
    contactRequest.priority = priority
    contactRequest.message = message
    contactRequest.Save()
    print(contactRequest)