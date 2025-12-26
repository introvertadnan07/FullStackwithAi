# # import sys
# # print(sys.version)




# response = client.chat.completions.create(
#     model="chatgpt-4o-latest",
#     response_format={"type": "json_object"},
#     messages=[
#         {"role": "system", "content": SYSTEM_PROMPT},
#         {"role": "user", "content": "Hey, write a code n numbers in js"},

#         {
#             "role": "assistant",
#             "content": json.dumps({
#                 "step": "START",
#                 "content": "You want a JavaScript code to add 'n' numbers."
#             })
#         },

#         {
#             "role": "assistant",
#             "content": json.dumps({
#                 "step": "PLAN",
#                 "content": "1. Ask for n.\n2. Loop n times.\n3. Sum numbers.\n4. Print result."
#             })
#         }
#     ]
# )

# print(response.choices[0].message.content)
