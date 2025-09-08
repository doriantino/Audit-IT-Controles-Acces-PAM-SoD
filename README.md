## Projet d'Audit IT Simulé

**Auteur :** Dorian Dikoume (Profil IT Advisory & Data Analyst)
**Date du Rapport :** 9 juillet 2025
**Période d'Audit Simulée :** Du 1er janvier 2025 au 30 janvier 2025

---

### 1. Introduction

Ce projet GitHub présente une simulation d'audit des contrôles d'accès logiques, avec un accent particulier sur la **Gestion des Comptes à Privilèges (PAM)** et la **Séparation des Tâches (SoD)** au sein de systèmes d'information critiques. Il a été conçu pour démontrer mes compétences en tant qu'**IT Audit & Advisory**, en abordant des problématiques réelles de sécurité, de fraude, d'erreur opérationnelle et de non-conformité réglementaire.

Dans un environnement numérique où les cybermenaces et les risques internes sont omniprésents, des contrôles d'accès robustes sont la pierre angulaire de la sécurité et de la conformité. Cet audit simulé illustre une approche rigoureuse pour identifier les faiblesses et proposer des recommandations concrètes.

L'audit a été réalisé en conformité avec les meilleures pratiques de l'industrie et les exigences réglementaires, s'appuyant notamment sur :

* Les directives de l'**ISO 27001** (Systèmes de Management de la Sécurité de l'Information) pour la gestion des accès et la sécurité opérationnelle.
* Les exigences du **Règlement Général sur la Protection des Données (RGPD)**, en particulier l'Article 32 relatif à la sécurité du traitement des données personnelles.
* Les principes du **Sarbanes-Oxley Act (SOX)**, notamment la Section 404 concernant les contrôles internes sur les rapports financiers, où la SoD joue un rôle crucial.
* Le cadre de gouvernance des TI **COBIT**, pour l'évaluation de la maturité et de l'efficacité des processus de contrôle.

Ce rapport vise à fournir une vision claire des faiblesses identifiées, de leurs risques associés, et des recommandations concrètes pour renforcer la posture de sécurité et de conformité d'une organisation.

---

### 2. Structure du Projet

Ce dépôt contient les éléments suivants :

* `README.md` : Ce fichier, présentant le projet.
* `audit_script.py` : Le script Python principal qui simule l'audit des logs d'accès, détecte les violations PAM et SoD, et génère des constats et recommandations.
* `synthetic_data_generation.py` (ou intégré dans `audit_script.py`) : Le module de génération des données d'audit synthétiques utilisées pour la simulation.

---

### 3. Installation et Utilisation

Pour exécuter le script d'audit :

1.  **Cloner le dépôt :**
    ```bash
    git clone https://github.com/votre_utilisateur/nom_du_depot.git
    cd nom_du_depot
    ```
2.  **Environnement Python :** Assurez-vous d'avoir Python 3.x installé. Il est recommandé d'utiliser un environnement virtuel :
    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Linux/macOS
    # ou `venv\Scripts\activate` sur Windows
    ```
3.  **Installer les dépendances :**
    ```bash
    pip install pandas
    ```
4.  **Exécuter le script d'audit :**
    ```bash
    python audit_script.py
    ```
    Le script générera un dataset synthétique en mémoire, effectuera l'audit et affichera les constats et recommandations directement dans la console.

---

### 4. Méthodologie d'Audit

L'audit simulé suit une approche structurée en plusieurs phases pour garantir une évaluation complète et rigoureuse des contrôles d'accès :

#### 4.1. Phase de Planification et Définition du Périmètre (Scoping)

* **Compréhension de l'environnement :** Analyse des objectifs métier de l'organisation et de l'architecture générale de ses systèmes d'information critiques (ERP, systèmes financiers, annuaires d'utilisateurs).
* **Identification des risques :** Revue des risques de sécurité et de fraude liés aux accès privilégiés et aux conflits de tâches.
* **Définition des critères d'audit :** Établissement des critères d'évaluation basés sur les politiques internes de l'organisation, et les référentiels externes (ISO 27001, RGPD, SOX, COBIT).
* **Délimitation du périmètre :** Focalisation sur les journaux d'activités des utilisateurs et les actions sur des contrôleurs considérés comme sensibles (`UserManagement`, `AdminPanel`, `Invoice`, `Payment`, `SystemConfig`, `Supplier`).

#### 4.2. Phase de Collecte d'Informations et de Preuves

* **Extraction des journaux d'activités :** Récupération des logs d'audit des systèmes cibles pour la période définie. Dans le cadre de cette simulation, un dataset synthétique est généré directement par le script pour représenter ces logs. Ce dataset inclut des informations sur l'utilisateur (`user_id`), le contrôleur (`controller`), l'action (`action`), la date et l'heure (`actiontime`), la durée de l'action (`duration`), et l'agent utilisateur (`useragent`).
* **Documentation :** Revue des politiques de sécurité des informations, des procédures de gestion des identités et des accès (IAM), et des matrices de séparation des tâches (si existantes).
* **Entretiens (simulés) :** Compréhension des processus auprès des équipes IT (administrateurs systèmes, sécurité) et des équipes métier (finance, RH) pour valider la compréhension des flux et des responsabilités.

#### 4.3. Phase de Tests et d'Analyse

* **Tests de conception :** Vérification de l'adéquation des politiques et procédures existantes avec les objectifs de sécurité et de conformité.
* **Tests d'efficacité opérationnelle :**
    * **Analyse des logs :** Application de règles d'analyse automatisées sur le dataset synthétique pour identifier des schémas d'activités anormaux ou des combinaisons d'actions conflictuelles.
    * **PAM :** Recherche d'activités privilégiées hors heures ouvrées, de durées de session anormales, de changements suspects d'agent utilisateur et de comptes privilégiés inactifs.
    * **SoD :** Détection de séquences d'actions par le même utilisateur qui violent les principes de séparation des tâches (ex: créer une facture et approuver un paiement).
    * **Validation :** Comparaison des résultats des analyses avec les critères d'audit définis.

#### 4.4. Phase de Reporting et Recommandations

* **Formalisation des constats :** Rédaction claire et factuelle des faiblesses identifiées, étayées par des exemples concrets tirés des données.
* **Analyse des risques :** Évaluation de l'impact potentiel (financier, opérationnel, réglementaire, réputationnel) de chaque constat.
* **Formulation de recommandations :** Proposition d'actions correctives concrètes, mesurables et alignées sur les meilleures pratiques et les exigences réglementaires.
* **Présentation :** Communication des résultats aux parties prenantes concernées.

---

### 5. Synthèse des Constats et Recommandations Clés

| Domaine d'Audit | Constats Majeurs | Risques Associés | Recommandations Clés |
| :-------------- | :--------------- | :--------------- | :------------------- |
| **PAM** | Activités hors heures ouvrées, Durées d'activité anormales, Changements suspects d'agent utilisateur, Comptes dormants. | Accès non autorisés, Compromission de comptes, Fraude interne, Fuite de données, Non-conformité RGPD/ISO 27001. | Implémentation de solution PAM, MFA, Politiques d'accès strictes, Surveillance en temps réel, Revues régulières des comptes. |
| **SoD** | Conflits de fonctions (ex: création de fournisseur + paiement), Cumul de privilèges. | Fraude financière, Erreurs opérationnelles, Non-conformité SOX/ISO 27001. | Révision des rôles et permissions, Matrice de SoD, Contrôles compensatoires, Outils d'analyse SoD. |

---

### 6. Constats Détaillés et Recommandations

#### 6.1. Gestion des Comptes à Privilèges (PAM)

Les comptes à privilèges (administrateurs systèmes, bases de données, applications critiques) sont des cibles privilégiées pour les attaquants. Une gestion inadéquate de ces comptes peut entraîner des conséquences désastreuses, allant de la fuite de données massives à l'interruption totale des opérations.

**Constats :**

* **Activités privilégiées hors heures ouvrées (Gravité : Moyenne)**
    * **Description :** L'analyse des journaux a révélé que des actions privilégiées ont été effectuées par des utilisateurs identifiés comme ayant des droits élevés (ex: `user_it_admin`) en dehors des plages horaires de travail habituelles (avant 8h ou après 18h). Ces activités peuvent indiquer une utilisation non autorisée, une négligence, ou une compromission des comptes.
    * *Exemple de constat simulé :* L'utilisateur `user_it_admin` a effectué une action privilégiée (`Access` sur `AdminPanel`) à `2025-01-15 21:35:12`.
    * **Risque Associé :** Augmentation du risque d'accès non autorisé et de manipulation malveillante des systèmes, rendant plus difficile la détection des incidents de sécurité.
    * **Lien Réglementaire :** Manquement aux principes de sécurité et de traçabilité des accès (Article 32 RGPD, ISO 27001 A.9.2.3).

* **Durée d'activité privilégiée anormalement longue (Gravité : Élevée)**
    * **Description :** Certaines sessions ou actions privilégiées ont montré des durées significativement plus longues que la moyenne statistique observée pour des activités similaires. Une durée excessive peut signaler une session laissée ouverte sans surveillance, une tentative d'exfiltration de données, ou une activité suspecte prolongée.
    * *Exemple de constat simulé :* L'utilisateur `user_it_admin` a effectué une action privilégiée (`Change_Settings` sur `SystemConfig`) avec une durée anormalement longue (`850s`) à `2025-01-20 10:45:00`.
    * **Risque Associé :** Vulnérabilité accrue aux attaques par "session hijacking", utilisation prolongée non surveillée des privilèges, et difficulté à identifier le moment précis d'une éventuelle compromission.
    * **Lien Réglementaire :** Non-conformité avec les exigences de surveillance et de gestion des incidents de sécurité (ISO 27001 A.12.6.1).

* **Changement suspect d'agent utilisateur pour un compte privilégié (Gravité : Élevée)**
    * **Description :** Il a été observé que des utilisateurs privilégiés ont changé d'agent utilisateur (c'est-à-dire le type de navigateur ou de système d'exploitation utilisé pour se connecter) en un laps de temps très court lors de l'exécution d'actions sensibles. Un tel changement rapide peut indiquer une tentative de contournement des contrôles, un partage de compte, ou une compromission d'identité.
    * *Exemple de constat simulé :* L'utilisateur privilégié `user_external_auditor` a changé d'agent utilisateur de `Mozilla/...Chrome` à `MaliciousAgent/1.0 (Linux)` en un court laps de temps lors d'actions privilégiées.
    * **Risque Associé :** Indication potentielle de compromission du compte ou d'un accès non autorisé, rendant la traçabilité des actions incertaine et augmentant le risque de fraude ou de fuite de données.
    * **Lien Réglementaire :** Manquement aux exigences de traçabilité et d'attribution des actions (RGPD Article 32, ISO 27001 A.9.4.1).

* **Comptes privilégiés dormants ou sporadiques (Gravité : Faible)**
    * **Description :** L'analyse a identifié des comptes privilégiés qui n'ont eu aucune activité ou une activité très faible sur la période d'audit. Ces comptes peuvent être des "comptes orphelins" (appartenant à des employés partis ou à des projets terminés) ou des comptes dont l'utilisation n'est pas correctement gérée, augmentant la surface d'attaque.
    * *Exemple de constat simulé :* Le compte privilégié `user_hr_01` n'a effectué aucune activité privilégiée sur la période d'audit.
    * **Risque Associé :** Vulnérabilité potentielle si ces comptes sont compromis, car leur inactivité les rend moins susceptibles d'être surveillés. Risque de non-conformité avec les politiques de gestion du cycle de vie des accès.
    * **Lien Réglementaire :** Manquement à l'ISO 27001 (A.9.2.1 "Enregistrement et déprovisionnement des utilisateurs").

**Recommandations :**

1.  **Implémenter une solution de Privileged Access Management (PAM) :** Déployer une solution PAM pour centraliser la gestion des identifiants (rotation automatique des mots de passe), la supervision des sessions en temps réel, l'enregistrement des frappes et la traçabilité granulaire de toutes les actions effectuées avec des comptes à privilèges.
2.  **Renforcer les politiques d'authentification :** Exiger systématiquement la Multi-Factor Authentication (MFA) pour tous les accès aux systèmes et applications critiques, en particulier pour les comptes à privilèges. Ceci est une mesure clé pour protéger la confidentialité et l'intégrité des données personnelles, conformément à l'**ISO 27001 (A.9.2.4)** et aux exigences de l'**Article 32 du RGPD**.
3.  **Définir et appliquer des plages horaires d'accès strictes :** Restreindre l'utilisation des comptes à privilèges aux heures de travail définies. Toute activité en dehors de ces plages doit déclencher une alerte et une justification documentée et approuvée.
4.  **Mettre en place une surveillance avancée et des alertes en temps réel :** Utiliser des outils SIEM (Security Information and Event Management) pour corréler les événements de logs et générer des alertes automatiques en cas de durées de session anormales, de changements d'agent utilisateur suspects, ou de toute activité sortant de la norme pour les comptes privilégiés.
5.  **Procéder à des revues régulières et rigoureuses des comptes à privilèges :** Mettre en place un processus formel de revue trimestrielle ou semestrielle des accès privilégiés pour identifier et désactiver/supprimer les comptes non nécessaires, dormants ou obsolètes, en ligne avec l'**ISO 27001 (A.9.2.1)**.

#### 6.2. Séparation des Tâches (SoD)

La Séparation des Tâches est un contrôle interne fondamental visant à prévenir la fraude et les erreurs en s'assurant qu'aucune personne ne détient un contrôle excessif sur un processus métier critique. Un conflit de SoD survient lorsqu'un utilisateur a la capacité d'exécuter des fonctions incompatibles qui, combinées, pourraient lui permettre de commettre une fraude sans détection.

**Constats :**

* **Conflits de séquence détectés dans les processus métier critiques (Gravité : Élevée)**
    * **Description :** L'analyse des journaux d'activités a révélé que certains utilisateurs ont effectué des séquences d'actions conflictuelles dans des applications métier critiques (ex: ERP), permettant potentiellement à une seule personne de contrôler un cycle complet (ex: création de fournisseur, saisie de facture, et exécution de paiement).
    * *Exemple de constat simulé :* L'utilisateur `user_finance_02` a effectué une séquence d'actions conflictuelles (`Invoice/Create, Payment/Approve`) dans une fenêtre de 60 minutes, ce qui constitue un conflit de Séparation des Tâches : Fraude - Création et approbation de paiement.
    * *Autre exemple de constat simulé :* L'utilisateur `user_it_admin` a effectué une séquence d'actions conflictuelles (`UserManagement/Edit_Permissions, AdminPanel/Access`) dans une fenêtre de 30 minutes, ce qui constitue un conflit de Séparation des Tâches : Abus de privilèges - Auto-attribution de droits.
    * **Risque Associé :** Risque élevé de fraude financière, d'erreurs opérationnelles non détectées, et de manipulation des données. Ces violations peuvent avoir des implications directes sur la fiabilité des rapports financiers, en contradiction avec les exigences du **SOX**.
    * **Lien Réglementaire :** Violation directe du **SOX (Section 404)** et manquement à l'**ISO 27001 (A.6.1.2 "Séparation des tâches")**.

**Recommandations :**

1.  **Réviser et optimiser la matrice de SoD et les rôles applicatifs :** Définir clairement les fonctions incompatibles au niveau des processus métier et s'assurer que les rôles et permissions dans les systèmes (notamment l'ERP) sont configurés pour empêcher le cumul de ces fonctions par un seul individu.
2.  **Mettre en œuvre des contrôles compensatoires robustes :** Lorsque la séparation stricte des tâches n'est pas réalisable pour des raisons opérationnelles (ex: petite équipe), des contrôles compensatoires efficaces doivent être mis en place. Cela inclut des revues indépendantes et documentées par un tiers (superviseur, autre département) des transactions à risque élevé. Ces contrôles doivent être régulièrement testés pour leur efficacité, en ligne avec le **SOX (Section 404)** et l'**ISO 27001 (A.6.1.2)**.
3.  **Utiliser des outils d'analyse de SoD :** Déployer des solutions logicielles dédiées à l'analyse des droits et des activités pour scanner régulièrement les conflits de SoD (à la both au niveau des rôles et des transactions) et générer des alertes proactives. Ces outils peuvent grandement faciliter la gestion de la SoD dans des environnements complexes.
4.  **Sensibilisation et formation continue :** Former régulièrement les utilisateurs, les managers et les équipes IT aux principes de la SoD, aux risques associés aux violations, et à l'importance de signaler toute anomalie ou tentative de contournement des contrôles.

---

### 7. Portée et Limitations de l'Audit

#### 7.1. Portée

Cet audit s'est concentré sur l'analyse des journaux d'activités des utilisateurs pour les contrôles d'accès privilégiés et la détection des conflits de séparation des tâches sur une sélection de contrôleurs et d'actions critiques. Les systèmes couverts par l'analyse des logs incluent des simulations de systèmes de gestion des utilisateurs, des panneaux d'administration, et des modules financiers/fournisseurs.

#### 7.2. Limitations

* **Données synthétiques :** Les données utilisées pour cet audit sont synthétiques et ne reflètent pas la complexité et le volume exacts des logs d'une organisation réelle. Les conclusions sont basées sur les schémas simulés.
* **Périmètre limité :** L'audit n'a pas couvert tous les types de contrôles d'accès (ex: accès physiques, accès réseau détaillés) ni tous les systèmes d'information de l'organisation.
* **Absence d'entretiens directs :** En tant qu'audit simulé, il n'a pas inclus d'entretiens directs avec toutes les parties prenantes, ce qui est crucial pour valider les processus et les contrôles compensatoires.
* **Règles simplifiées :** Les règles d'audit implémentées sont des simplifications de la réalité et ne couvrent pas toutes les nuances possibles des attaques ou des violations de SoD.

Malgré ces limitations, cet audit fournit une base solide pour comprendre les risques liés aux contrôles d'accès et les pistes d'amélioration.

---

### 8. Conclusion et Prochaines Étapes

Cet audit a mis en évidence des domaines d'amélioration significatifs dans la gestion des contrôles d'accès, tant au niveau des comptes à privilèges que de la séparation des tâches. La mise en œuvre des recommandations proposées permettra à l'organisation de renforcer sa posture de sécurité, de réduire son exposition aux risques de fraude et d'erreur, et d'assurer une meilleure conformité avec les réglementations en vigueur (RGPD, SOX) et les bonnes pratiques (ISO 27001, COBIT).

**Prochaines étapes suggérées :**

* **Priorisation des recommandations :** Établir un plan d'action avec des priorités basées sur le niveau de risque et la faisabilité.
* **Mise en œuvre :** Allouer les ressources nécessaires à l'implémentation des recommandations.
* **Suivi régulier :** Mettre en place un mécanisme de suivi pour s'assurer que les recommandations sont mises en œuvre efficacement et que les contrôles restent opérationnels.
* **Audits futurs :** Planifier des audits de suivi pour évaluer l'efficacité des actions correctives et l'évolution de la posture de sécurité.

---

### 9. Contribuer

Les contributions à ce projet sont les bienvenues ! Si vous souhaitez améliorer le script d'audit, ajouter de nouvelles règles, ou étendre la génération de données synthétiques, n'hésitez pas à soumettre une *pull request* ou à ouvrir une *issue*.
