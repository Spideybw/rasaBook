import sqlite3


# # class ActionHelloWorld():

#     # def name(self) -> Text:
#     #     return "action_activity_information"

# def run():
# conn = sqlite3.connect('rasa.db')
# c = conn.cursor()   
# username = "ybw"
# print(username)
# c.execute("INSERT INTO user(name,gender,STU_EMAIL) VALUES(?,?,?)",(str(username),int(1),"123@gmail.com"))
# print("success")
# conn.commit()
# c.close()
#         # print(activity_name)
#         conn = sqlite3.connect('rasa.db')
#         c = conn.cursor()   
#         c.execute("SELECT * from activity WHERE name = ?",("AAActivity",))
#         result = c.fetchone()
#         # print(result)
#         if result != None:
#           print("Activity name:" + result[0] + "\n" + 
#                                         "start date:" + "\n" +
#                                         "ticket price" + str(result[2]) + "\n" +
#                                         "organizer:" + result[3] + "\n"
#                                         "description:" + result[4] + "\n")
#         #   dispatcher.utter_message(text="Activity name:" + result[0] + "\n" + 
#         #                                 "start date:" + "\n" +
#         #                                 "ticket price" + result[2] + "\n" +
#         #                                 "organizer:" + result[3] + "\n"
#         #                                 "description:" + result[4] + "\n")
#         #   print()
#         else:
#             # dispatcher.utter_message(text="not exist")
#             print("nononono")
#         c.close()


# run()
#         # dispatcher.utter_message(text="Hello World!")

#         # return []
# conn = sqlite3.connect('rasa.db')
# c = conn.cursor()   
# c.execute("SELECT * FROM book WHERE user_name = ?",("Spideybw",))
# result = c.fetchall()
# print(result[0])
# res = "your book list:"

# for re in result:  
#     res = res + "\n" + "id:" + str(re[0]) + "   activity:" +  str(re[1])

# print(res)        

# c = conn.cursor()   
# c.execute("INSERT INTO book(activity_name,user_name) VALUES(?,?)",("AAActivity","ybw"))
# print(1)
# conn.commit()
# result = c.fetchall()
# print(result[0])
# res = "activity name list:"
# for re in result:  
#     res = res + "\n" + str(re[0])
# print(res)