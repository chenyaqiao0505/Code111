from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = "AC06f9ba1fa660248daebf9be002beb788"
# Your Auth Token from twilio.com/console
auth_token  = "b756b66b918b48f02e1adb1c0166578d"
client = Client(account_sid, auth_token)
message = client.messages.create(
    to="+8615732671356",
    # to = '+8618632614072',
    from_="18135444388",
    body="我是秦始皇。我没死，我是吃了长生不老药的，我告诉你啊，我在陕西有3000吨黄金和300万秦兵被封印，现在只需要198元就能解封，只要你打钱给我，待我解封之日，我就收你当干儿子，立你为太子！君无戏言。")
