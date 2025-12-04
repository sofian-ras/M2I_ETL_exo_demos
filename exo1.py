import requests
import pandas as pd

BASE_URL = "https://jsonplaceholder.typicode.com"
POST_URL = f"{BASE_URL}/posts"


url_user = f"{BASE_URL}/users"
response = requests.get(url_user)
response.raise_for_status()

print(f"Statut : {response.status_code}")

print("Contenu brut en .text :")
print(response.text)

print("Contenu en json : ")
donnees = response.json()
print(donnees)

# affhicer nom et email
for user in donnees:
    print(f"Nom : {user['name']}, Email : {user['email']}")

user_id = requests.get(f"{POST_URL}?userId=1")
user_id.raise_for_status()

posts_response = requests.get(POST_URL)
posts_response.raise_for_status()
posts = posts_response.json()

df = pd.DataFrame(posts)
counts = df.groupby("userId").size()
print(counts)


url_commentaires = f"{BASE_URL}/comments?postId=1"

response_commentaires = requests.get(url_commentaires)
response_commentaires.raise_for_status()
total_comms = response_commentaires.json()

print(f"nombre de commentaires du post 1 : {len(total_comms)}")
for tot_c in total_comms:
    print(f"- {tot_c['name']} : {tot_c['email']}")

# ----------------------------------

rows =[]

for post in posts[:10]:
    post_id = post["id"]
    post_title = post["title"]

comm_reccup = requests.get(f"{BASE_URL}/comments?postId={post_id}")
comm_reccup.raise_for_status()
comm = comm_reccup.json()

rows.append({
    "post_id": post_id,
    "post_title": post_title,
    "nombre_commentaire": len(comm)
})

df_posts_comm = pd.DataFrame(rows)
print("dataframe des 10 premieres lignes :")
print(df_posts_comm)

df_posts_comm.to_csv("posts_commentaires.csv", index=False)
print("csv posts_commentaires.csv enregistré")
