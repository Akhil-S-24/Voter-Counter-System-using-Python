
import pandas as pd
import matplotlib.pyplot as plt
import time


candidates = ["ram", "Kavana", "shan", "vijay"]


votes = {candidate: 0 for candidate in candidates}


voted_users = set()

print("===== 🗳️ WELCOME TO SMART VOTING SYSTEM =====\n")
print("Candidates:")
for i, candidate in enumerate(candidates, start=1):
    print(f"{i}. {candidate}")


num_voters = int(input("\nEnter total number of voters: "))


for i in range(num_voters):
    print(f"\nVoter {i+1}:")

    user_id = input("Enter your Voter ID: ")
    if user_id in voted_users:
        print("❌ You have already voted! One vote per person allowed.")
        continue
    voted_users.add(user_id)

    for j, candidate in enumerate(candidates, start=1):
        print(f"{j}. {candidate}")

    choice = int(input("Enter your vote (1-4): "))
    
    if 1 <= choice <= len(candidates):
        selected = candidates[choice - 1]
        votes[selected] += 1
        print(f"✅ You voted for {selected}")
    else:
        print("❌ Invalid choice. Vote not counted.")
    time.sleep(0.5)

print("\n===== 🧾 FINAL POLL RESULTS =====")
total_votes = sum(votes.values())

for candidate, count in votes.items():
    percent = (count / total_votes) * 100 if total_votes > 0 else 0
    print(f"{candidate}: {count} votes ({percent:.2f}%)")


winner = max(votes, key=votes.get)
print("\n🏆 Winner is:", winner)
print("=============================")


df = pd.DataFrame(list(votes.items()), columns=["Candidate", "Votes"])


plt.figure(figsize=(8, 5))
plt.bar(df["Candidate"], df["Votes"], color=["#00C49F", "#FFBB28", "#FF8042", "#0088FE"])
plt.title("📊 Voting Results")
plt.xlabel("Candidates")
plt.ylabel("Number of Votes")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
