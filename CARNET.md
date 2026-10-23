# 📒 Mon carnet de bord

**Nom :** Niri

**Prénom :** Nouha

**Adresse de mon site :** https://nina06.pythonanywhere.com

> Modifiez ce fichier directement sur GitHub (icône crayon ✏️) pour répondre aux questions de chaque exercice.
> Écrivez avec vos propres mots : une réponse courte et juste vaut mieux qu'un long copier-coller ! 🙂

---

## 🟢 Exercice 1 — Mon premier déploiement

1. Où se trouve physiquement le code qui fabrique votre page : sur votre ordinateur, sur GitHub ou sur PythonAnywhere ?

   > Le code est stocké sur GitHub et exécuté sur PythonAnywhere pour fabriquer la page Web. 

2. Pourquoi votre voisin(e) peut-il voir votre site, alors que vous n'avez rien installé sur son ordinateur ?

   > Parce que le site est hébergé sur un serveur accessible par Internet. Son navigateur demande la page au serveur.

---

## 🟢 Exercice 2 — Les URL et les routes

1. Dans l'URL `https://www.google.com/maps`, quel est le nom de domaine ? Quel est le chemin ?

   > Le domaine est www.google.com et le chemin est /maps.

2. Que veut dire le message *Not Found* ? Qui l'a envoyé : votre navigateur ou le serveur ?

   >Cela signifie que la page demandée n’existe pas ou n’a pas été trouvée. Le serveur renvoie généralement le code HTTP 404.



3. Que se passe-t-il si deux fonctions portent le même nom dans `flask_app.py` ? (Indice : essayez, puis lisez l'Error log.)

   > ela peut provoquer un conflit dans Flask et une erreur au démarrage du site, notamment si deux routes sont associées à la même fonction de manière incorrecte.

---

## 🔵 Exercice 3 — Le langage HTML

1. Quelle est la différence entre ce que le serveur **envoie** et ce que le navigateur **affiche** ?

   > Le serveur envoie du code HTML et le navigateur l'interprète pour afficher une page lisible.
2. À quoi servent les balises `<h1>`, `<p>`, `<ul>` et `<li>` ?

   > <h1> sert à un titre principal, <p> à un paragraphe, <ul> à une liste et <li> à un élément de liste. 

3. Pourquoi l'image s'affiche-t-elle alors qu'elle n'est pas sur votre serveur ?

   > Parce que l'image est hébergée sur un autre serveur et que le navigateur la télécharge depuis son adresse.
---

## 🔵 Exercice 4 — Les templates

1. Pourquoi est-ce une bonne idée de séparer le code Python et le HTML ? (Pensez à une équipe avec un développeur et un graphiste.)

   > ela rend le projet plus facile à comprendre et à modifier. Le développeur s'occupe du code Python et le graphiste de la présentation HTML.


2. Les `{{ prenom }}` sont-ils remplacés par le serveur ou par le navigateur ? Comment l'avez-vous vérifié ?

   > next<

---

## 🔵 Exercice 5 — Le CSS et les liens

1. Quelle est la différence de rôle entre le HTML et le CSS ?

   > Le HTML organise le contenu de la page. Le CSS définit son apparence, comme les couleurs, les tailles et la mise en page

2. Pour afficher votre page `/presentation`, combien de fichiers le navigateur doit-il télécharger ? (Vous pourrez le vérifier à l'exercice suivant !)

   > Cela dépend des ressources utilisées par la page. Le navigateur télécharge le document HTML et les fichiers nécessaires, comme le CSS et les images. Je peux compter les requêtes dans l'onglet Réseau du navigateur.

3. Pourquoi faut-il parfois faire **Ctrl + F5** pour voir les changements de CSS ?

   > Le navigateur garde parfois l’ancienne version du CSS en mémoire. Ctrl + F5 force le rechargement des fichiers.
---

## 🟣 Exercice 6 — Espionner le navigateur

1. Que signifie HTTP ? Qui envoie la **requête** et qui envoie la **réponse** ?

   >HTTP signifie HyperText Transfer Protocol. Le navigateur envoie la requête et le serveur envoie la réponse.

2. Combien de requêtes votre page `/presentation` a-t-elle déclenchées ? Lesquelles ?

   > Je dois regarder le nombre de requêtes dans l’onglet Réseau du navigateur. Elles peuvent concerner le HTML, le CSS, les images et la favicon.

3. Que signifie le code `200` ? Et le code `404` de la favicon ?

   > Le code 200 signifie que la requête a réussi. Le code 404 signifie que la favicon demandée n’a pas été trouvée. 

4. Pourquoi les modifications faites dans l'onglet Éléments ne sont-elles pas visibles par les autres visiteurs ?

   > Parce que ces modifications changent uniquement l’affichage dans mon navigateur et ne modifient pas le site sur le serveur.

---

## 🟣 Exercice 7 — Envoyer des informations dans l'URL

1. Dans l'URL `https://www.youtube.com/results?search_query=chat`, quel est le nom du paramètre ? Quelle est sa valeur ?

   > Le paramètre est search_query et sa valeur est chat.

2. Pourquoi le serveur plante-t-il avec `a=bonjour` ? Que faudrait-il faire pour l'éviter ?

   > Le code essaie probablement de traiter « bonjour » comme un nombre. Il faut vérifier les données reçues et gérer les erreurs.

3. Pourquoi est-il dangereux d'afficher **tel quel** ce que l'utilisateur envoie ?

   > Parce qu’un utilisateur pourrait envoyer du code malveillant. Il faut vérifier et afficher les données de manière sécurisée.

---

## 🟣 Exercice 8 — Les formulaires

1. Quelle est la différence visible entre GET et POST ?

   > Avec GET, les données apparaissent généralement dans l’URL. Avec POST, elles sont envoyées dans le corps de la requête.

2. Pour un formulaire de **recherche**, quelle méthode choisiriez-vous ? Et pour un formulaire de **connexion avec mot de passe** ? Pourquoi ?

   > Je choisirais GET pour une recherche, car on peut partager l’URL des résultats. Pour une connexion, je choisirais POST avec HTTPS pour protéger le mot de passe pendant le transport.

3. Les données envoyées en POST sont-elles vraiment « secrètes » ? (Pensez à ce que vous avez vu dans l'onglet Réseau.)

   > Non. Elles peuvent être visibles dans les outils de développement. HTTPS est nécessaire pour chiffrer les données pendant leur transport.

---

## 🔴 Exercice 9 — Les codes de statut

1. Quelle est la différence entre une erreur `4xx` et une erreur `5xx` ? Qui est « fautif » dans chaque cas ?

   > Les erreurs 4xx indiquent généralement un problème dans la requête du client. Les erreurs 5xx indiquent un problème côté serveur.

2. Comment fonctionne une redirection ? Qui fait la deuxième requête : le serveur ou le navigateur ?

   >  Le serveur indique une nouvelle adresse avec un code de redirection. C’est ensuite le navigateur qui effectue la deuxième requête.

3. Donnez un exemple de situation où un vrai site utilise une redirection.

   > Un site peut rediriger une adresse HTTP vers la version sécurisée HTTPS.

---

## 🔴 Exercice 10 — Ce que le serveur sait de vous

1. Citez trois informations que le serveur connaît sur vous, sans que vous ayez rien rempli.

   > Mon adresse IP, le type de navigateur que j’utilise et la langue préférée indiquée par mon navigateur.

2. À quoi peut servir l'en-tête `Accept-Language` pour un site comme Wikipédia ?

   > Cet en-tête permet au site de connaître les langues préférées du navigateur et de proposer une langue adaptée. 

3. Dans l'Access log, retrouvez une requête qui a reçu un code `404`. Quelle page était demandée ?

   > Je dois consulter l’Access log de PythonAnywhere et relever le chemin de la requête ayant reçu le code 404. 

4. Après cet exercice, que pensez-vous de la notion de « navigation anonyme » ?

   > La navigation n’est pas totalement anonyme, car le serveur reçoit certaines informations techniques, comme l’adresse IP. La navigation privée ne rend pas invisible sur Internet.

---

## 🔴 Exercice 11 — Le Web des machines : API et JSON

1. Quelle est la différence entre une page HTML et une réponse JSON ? À qui chacune est-elle destinée ?

   > HTML sert à afficher une page dans un navigateur. JSON sert à échanger des données structurées entre des programmes. 

2. Dans la page `/horloge`, quel code s'exécute sur le **serveur** et quel code s'exécute dans le **navigateur** ?

   > Le code Python s’exécute sur le serveur. Le JavaScript de la page s’exécute dans le navigateur, si la page en utilise. 

3. Citez une application de votre téléphone qui, selon vous, utilise une API. Quelles données échange-t-elle ?

   > Une application météo utilise une API pour récupérer la température, les prévisions et les conditions météorologiques.

---

## 🏁 Pour conclure

En quelques phrases, expliquez à un ami ce qui se passe entre le moment où il tape une adresse dans son navigateur et celui où la page s'affiche :

> Quand je tape une adresse, mon navigateur envoie une requête au serveur. Le serveur traite la demande et renvoie une réponse contenant le contenu de la page. Le navigateur interprète le HTML et le CSS, télécharge les ressources nécessaires et affiche la page à l’écran.
