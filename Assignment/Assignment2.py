def count_msgs_by_user(messages):
    counts = {}
    for m in messages:
        user, _ = m.split(":", 1)
        user = user.strip()
        counts[user] = counts.get(user, 0) + 1
    print("Message count by user:")
    for user, cnt in counts.items():
        print(f"{user}: {cnt}")

def count_happy_messages(messages):
    happy_keywords = ["🙂", "😃", "happy"]
    count = 0
    for m in messages:
        text = m.split(":", 1)[1].lower()
        if any(h in text for h in happy_keywords):
            count += 1
    print(f"Number of happy messages: {count}")

def most_questions(messages):
    from collections import Counter
    counter = Counter()
    for m in messages:
        user, text = m.split(":", 1)
        if text.strip().endswith("?"):
            counter[user.strip()] += 1
    if counter:
        user, n = counter.most_common(1)[0]
        print(f"User who asked most questions: {user} ({n} question{'s' if n>1 else ''})")
    else:
        print("No questions asked.")

if __name__ == "__main__":
    n = int(input("Enter number of messages: "))
    messages = [input() for _ in range(n)]

    count_msgs_by_user(messages)
    count_happy_messages(messages)
    most_questions(messages)
