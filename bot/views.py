from django.shortcuts import render, HttpResponse
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Sender
import os

account_sid = 'ACb4b13b35c1e8403a020aa70776729ea9'
auth_token = '080ea2e37f1bee1330e53aa0a7f2cb49'
client = Client(account_sid, auth_token)

@csrf_exempt
def bot(request):
    phone_number = request.POST.get('From', '').replace('whatsapp:', '').strip()
    incoming_msg = request.POST.get('Body', '')
    sender, created = Sender.objects.get_or_create(phone_number=phone_number)
    
    resp = MessagingResponse()
    msg = resp.message()
    
    if created:
        response = (
            "היי,\n"
            "אני שמח שפנית אליי,\n"
            "אשתדל לענות לך בהקדם האפשרי.\n"
            "בנתיים אשמח לשמוע במה אוכל לעזור?\n"
            "\n"
            "שלח/י חזרה את המספר הרלוונטי:\n"
            "1.פתרונות לניהול לקוחות\n"
            "2.פתרונות לניהול פרויקטים\n"
            "3.פתרונות לניהול משאבים\n"
            "4.פתרונות לניהול מידע פיננסי\n"
            "5.פיתוח מערכות ופתרונות מותאמים אישית\n"
            "6.הדרכות Excel ו VBA לארגונים, עסקים ופרטיים\n"
            "\n"
            "נדבר בקרוב,\n"
            "רועי קליין Excel Road\n"
            "www.excel-road.com"
            )
    else:
        if incoming_msg == '1':
            response = (
                "בחרת את מספר 1 - פתרונות לניהול לקוחות\n"
                "ישנם הרבה אפשרויות לניהול לקוחות\n"
                "מדוחות אקסל למערכות CRM\n"
                "אשמח לשמוע איזה סוג עסק זקוק לניהול לקוחות\n"
                "לפי סוג העסק אוכל לייעץ לגבי הפתרון הטוב ביותר"
                )
        elif incoming_msg == '2':
            response = (
                "בחרת מספר 2 - פתרונות לניהול פרויקטים\n"
                "ישנם הרבה אפשרויות לניהול פרויקטים\n"
                "ישנן מערכות ייעודיות לכך ואפשר גם לעבוד עם אקסל\n"
                "אשמח לשמוע לגבי סוגי הפרויקטים ואיך עובדים היום?"
                )
        elif incoming_msg == '3':
            response = (
                "בחרת מספר 3 - פתרונות לניהול משאבים\n"
                "ניהול משאבים הינו דבר אינו פשוט, במיוחד עם מדובר על הרבה סוגים של משאבים\n"
                "אשמח לשמוע לגבי סוג העסק ואילו משאבים מנהלים בעסק?"
                )
        elif incoming_msg == '4':
            response = (
                "בחרת מספר 4 - פתרונות לניהול מידע פיננסי\n"
                "אם יש דבר חשוב לנהל אותו כמו שצריך זה זה.\n"
                "ישנן הרבה דרכים לניהול המידע הפיננסי שלנו והכל תלוי באיזה מידע מדובר\n"
                "האם מדובר בניהול מידע אישי או עבור העסק?"
                )
        elif incoming_msg == '5':
            response = (
                'בחרת מספר 5 - פיתוח מערכות ופתרונות מותאמים אישית\n'
                'פיתוח מערכת אינה החלטה של מה בכך\n'
                'אשמח אם נוכל להפגש ולדבר על הצרכים ומשאבים הנדרשים\n'
                'האם יש אפשרות לקבוע פגישה?\n'
                'אשמח לשמוע מתי את/ה פנוי/ה כדי להפגש'
                )
        elif incoming_msg == '6':
            response = (
                'בחרת מספר 6 - הדרכות Excel ו VBA לארגונים, עסקים ופרטיים\n'
                'אשמח לשמוע מי צריך את ההדרכה\n'
                'האם מדובר בעובדים של הארגון או שאת/ה צריך הדרכה פרטית?\n'
                'אשמח לשמוע מתי אוכל להתקשר או לקבוע פגישה, כמובן לפי העדפה שלך'
                )
    
    msg.body(response)
    return HttpResponse(str(resp), content_type="application/xml")
    
    
    
    