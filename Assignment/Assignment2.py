from collections import Counter, defaultdict

def count_total_messages(messages):
    print(f"Total messages: {len(messages)}")

def unique_users(messages):
    users = {msg.split(":", 1)[0].strip() for msg in messages}
    print(f"Unique users in the chat: {users}")

def total_words(messages):
    total = sum(len(msg.split(":", 1)[1].split()) for msg in messages)
    print(f"Total words in the chat: {total}")

def average_words(messages):
    total = sum(len(msg.split(":", 1)[1].split()) for msg in messages)
    avg = total / len(messages) if messages else 0
    print(f"Average words per message: {round(avg, 2)}")

def longest_message(messages):
    longest = max(messages, key=lambda m: len(m.split(":", 1)[1]), default="")
    print(f'Longest message: "{longest}"')

def most_active_user(messages):
    user_counts = Counter(msg.split(":")[0].strip().lower() for msg in messages)
    if user_counts:
        user, cnt = user_counts.most_common(1)[0]
        print(f"Most active user: {user} ({cnt} messages)")
    else:
        print("No messages.")

def user_message_count(messages, user):
    user = user.lower()
    count = sum(1 for msg in messages if msg.split(":")[0].strip().lower() == user)
    print(f"Messages sent by {user}: {count}")

def most_frequent_word_by_user(messages, user):
    user = user.lower()
    words = []
    for msg in messages:
        name, _, text = msg.partition(":")
        if name.strip().lower() == user:
            words += [w.strip('.,?!').lower() for w in text.strip().split()]
    if words:
        counter = Counter(words)
        most = counter.most_common(1)[0][0]
        print(f'Most frequent word used by {user}: "{most}"')
    else:
        print(f"No messages by {user}")

def first_and_last_by_user(messages, user):
    user = user.lower()
    user_msgs = [m for m in messages if m.split(":")[0].strip().lower() == user]
    if not user_msgs:
        print(f"No messages by {user}")
        return
    print(f'First message by {user}: "{user_msgs[0]}"')
    print(f'Last message by {user}: "{user_msgs[-1]}"')

def is_user_present(messages, user):
    user = user.lower()
    users = {msg.split(":", 1)[0].strip().lower() for msg in messages}
    if user in users:
        print(f"User '{user}' is present in the chat.")
    else:
        print(f"User '{user}' not found in the chat.")

def repeated_words(messages):
    all_words = [w.strip('.,?!').lower() for m in messages for w in m.split(":", 1)[1].split()]
    counter = Counter(all_words)
    common = {word for word, cnt in counter.items() if cnt > 1}
    print(f"Common repeated words: {common}")

def user_with_longest_avg_message(messages):
    user_lengths = defaultdict(list)
    for msg in messages:
        name, _, text = msg.partition(":")
        words = text.strip().split()
        user_lengths[name.strip().lower()].append(len(words))
    user_avgs = {u: (sum(lengths)/len(lengths)) for u, lengths in user_lengths.items()}
    if user_avgs:
        user = max(user_avgs, key=user_avgs.get)
        print(f"User with longest average message: {user} (avg {round(user_avgs[user], 2)} words)")
    else:
        print("No messages.")

def message_mentions(messages, username):
    username = username.lower()
    count = sum(1 for m in messages if username in m.split(":", 1)[1].lower())
    print(f"Messages mentioning '{username}': {count}")

def remove_duplicates(messages):
    unique = list(dict.fromkeys(messages))
    print(f"Unique messages count: {len(unique)}")
    # Uncomment to print unique messages:
    # for msg in unique:
    #     print(msg)

def sort_messages(messages):
    for m in sorted(messages, key=lambda x: x.lower()):
        print(m)

def extract_questions(messages):
    questions = [m for m in messages if "?" in m.split(":", 1)[1]]
    for q in questions:
        print(q)

def reply_ratio(messages, userA, userB):
    userA = userA.lower()
    userB = userB.lower()
    count = 0
    prev_user = None
    for msg in messages:
        user, _, _ = msg.partition(":")
        user = user.strip().lower()
        if prev_user == userA and user == userB:
            count += 1
        prev_user = user
    print(f"Reply ratio from {userB} to {userA}: {count} replies")

def deleted_messages(messages):
    count = sum(1 for m in messages if m.split(":", 1)[1].strip() == "This message was deleted")
    print(f"Deleted messages found: {count}")

def main():
    n = int(input("Enter the number of messages: "))
    messages = []
    for _ in range(n):
        while True:
            msg = input()
            if ":" in msg:
                messages.append(msg)
                break
            else:
                print("Invalid format. Please enter message as 'Name: message'.")

    options = [
        "Count total number of messages",
        "Identify unique users in the chat",
        "Count total words in the chat",
        "Calculate average words per message",
        "Find the longest message sent",
        "Find the most active user",
        "Get message count for a specific user",
        "Find the most frequently used word by a specific user",
        "Retrieve the first and last message sent by a user",
        "Check if a user is present in the chat",
        "Find commonly repeated words",
        "(option 12 skipped)",
        "Identify the user with the longest average message length",
        "Count how many messages mention a specific user",
        "Remove duplicate messages",
        "Sort messages alphabetically",
        "Extract all questions asked in the chat",
        "Calculate the reply ratio between two users",
        "Check for deleted messages"
    ]

    while True:
        print("\nAnalysis Options:")
        for idx, opt in enumerate(options, 1):
            print(f"{idx}. {opt}")
        num = input("Choose an option (or press enter to quit): ")
        if not num:
            print("Exiting.")
            break

        if not num.isdigit():
            print("Please enter a valid number option.")
            continue

        num = int(num)
        print(f"[DEBUG] You selected option: {num}")

        if num == 1:
            count_total_messages(messages)
        elif num == 2:
            unique_users(messages)
        elif num == 3:
            total_words(messages)
        elif num == 4:
            average_words(messages)
        elif num == 5:
            longest_message(messages)
        elif num == 6:
            most_active_user(messages)
        elif num == 7:
            user = input("Input user: ")
            user_message_count(messages, user)
        elif num == 8:
            user = input("Input user: ")
            most_frequent_word_by_user(messages, user)
        elif num == 9:
            user = input("Input user: ")
            first_and_last_by_user(messages, user)
        elif num == 10:
            user = input("Input user: ")
            is_user_present(messages, user)
        elif num == 11:
            repeated_words(messages)
        elif num == 12:
            print("Option 12 is not implemented.")
        elif num == 13:
            user_with_longest_avg_message(messages)
        elif num == 14:
            user = input("Input user: ")
            message_mentions(messages, user)
        elif num == 15:
            remove_duplicates(messages)
        elif num == 16:
            sort_messages(messages)
        elif num == 17:
            extract_questions(messages)
        elif num == 18:
            userA = input("User A: ")
            userB = input("User B: ")
            reply_ratio(messages, userA, userB)
        elif num == 19:
            deleted_messages(messages)
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

#output
'''Enter the number of messages: 6
Vikash: Good morning!
Sanjay: Hi Vikash, how are you?
Vikash: I am happy to see you, Sanjay!
Sanjay: I am happy too! Want to play chess?
Vikash: Sure, let's play!
Sanjay: Who will go first?

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (option 12 skipped)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
Choose an option (or press enter to quit): 1
[DEBUG] You selected option: 1
Total messages: 6

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (option 12 skipped)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
Choose an option (or press enter to quit): 2
[DEBUG] You selected option: 2
Unique users in the chat: {'Vikash', 'Sanjay'}

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (option 12 skipped)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
Choose an option (or press enter to quit): 3
[DEBUG] You selected option: 3
Total words in the chat: 29

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (option 12 skipped)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
Choose an option (or press enter to quit): 4
[DEBUG] You selected option: 4
Average words per message: 4.83

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (option 12 skipped)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
Choose an option (or press enter to quit): 5
[DEBUG] You selected option: 5
Longest message: "Sanjay: I am happy too! Want to play chess?"

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (option 12 skipped)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
Choose an option (or press enter to quit): 6
[DEBUG] You selected option: 6
Most active user: vikash (3 messages)

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (option 12 skipped)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
Choose an option (or press enter to quit): 7
[DEBUG] You selected option: 7
Input user: vikash
Messages sent by vikash: 3

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (option 12 skipped)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
Choose an option (or press enter to quit): 8
[DEBUG] You selected option: 8
Input user: sanjay
Most frequent word used by sanjay: "hi"

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (option 12 skipped)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
Choose an option (or press enter to quit): 9
[DEBUG] You selected option: 9
Input user: vikash
First message by vikash: "Vikash: Good morning!"
Last message by vikash: "Vikash: Sure, let's play!"

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (option 12 skipped)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
Choose an option (or press enter to quit): 10
[DEBUG] You selected option: 10
Input user: sanjay
User 'sanjay' is present in the chat.

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (option 12 skipped)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
Choose an option (or press enter to quit): 11
[DEBUG] You selected option: 11
Common repeated words: {'to', 'play', 'you', 'happy', 'i', 'am'}

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (option 12 skipped)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
Choose an option (or press enter to quit): Vikash: Good morning!
Sanjay: Hi Vikash, how are yPlease enter a valid number option.

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (option 12 skipped)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
Choose an option (or press enter to quit): ou?
Vikash: I am happy to see you, Sanjay!
Sanjay:Please enter a valid number option.

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (option 12 skipped)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
Choose an option (or press enter to quit): Please enter a valid number option.

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (option 12 skipped)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
Choose an option (or press enter to quit):  I am happy too! Want to play chess?
Vikash: Sure,Please enter a valid number option.

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (option 12 skipped)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
Choose an option (or press enter to quit):  let's play!
Sanjay: Who will go first?Please enter a valid number option.

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (option 12 skipped)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
Choose an option (or press enter to quit): 12
Please enter a valid number option.

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (option 12 skipped)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
Choose an option (or press enter to quit): 13
[DEBUG] You selected option: 13
User with longest average message: sanjay (avg 5.67 words)

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (option 12 skipped)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
Choose an option (or press enter to quit): 14
[DEBUG] You selected option: 14
Input user: vikash
Messages mentioning 'vikash': 1

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (option 12 skipped)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
Choose an option (or press enter to quit): 15
[DEBUG] You selected option: 15
Unique messages count: 6

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (option 12 skipped)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
Choose an option (or press enter to quit): 16
[DEBUG] You selected option: 16
Sanjay: Hi Vikash, how are you?
Sanjay: I am happy too! Want to play chess?
Sanjay: Who will go first?
Vikash: Good morning!
Vikash: I am happy to see you, Sanjay!
Vikash: Sure, let's play!

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (option 12 skipped)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
Choose an option (or press enter to quit): 17
[DEBUG] You selected option: 17
Sanjay: Hi Vikash, how are you?
Sanjay: I am happy too! Want to play chess?
Sanjay: Who will go first?

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (option 12 skipped)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
Choose an option (or press enter to quit): 18
[DEBUG] You selected option: 18
User A: vikash
User B: sanjay
Reply ratio from sanjay to vikash: 3 replies

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (option 12 skipped)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
Choose an option (or press enter to quit): 19
[DEBUG] You selected option: 19
Deleted messages found: 0

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (option 12 skipped)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
Choose an option (or press enter to quit): 
Exiting.'''