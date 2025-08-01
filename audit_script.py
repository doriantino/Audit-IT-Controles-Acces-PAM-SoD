import pandas as pd
from datetime import datetime, timedelta
import random # Pour générer des données synthétiques

# --- 1. Ingestion et Préparation des Données (Génération de données synthétiques) ---

def generate_synthetic_audit_data(num_records=1000):
    """Génère un dataset d'audit synthétique pour simuler des scénarios PAM et SoD."""
    data = []
    start_date = datetime(2025, 1, 1, 8, 0, 0)
    
    users = ['user_finance_01', 'user_it_admin', 'user_hr_01', 'user_sales_01', 'user_finance_02', 'user_external_auditor']
    
    controllers = ['Dashboard', 'Report', 'Invoice', 'Payment', 'UserManagement', 'AdminPanel', 'HRData', 'SalesCRM', 'SystemConfig', 'Supplier']
    
    actions = {
        'Dashboard': ['View'],
        'Report': ['Generate', 'View'],
        'Invoice': ['Create', 'View', 'Approve', 'Edit'],
        'Payment': ['Approve', 'Execute', 'View'],
        'UserManagement': ['Create_User', 'Edit_Permissions', 'Delete_User', 'View_Logs'],
        'AdminPanel': ['Access', 'Change_Settings', 'View_Logs'],
        'HRData': ['View', 'Edit_Salary'],
        'SalesCRM': ['Add_Lead', 'Update_Opportunity'],
        'SystemConfig': ['Modify_Config', 'View_Config'],
        'Supplier': ['Create', 'Edit']
    }

    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
        "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36",
        "CustomAgent/1.0 (AuditTool)", # Agent suspect
        "OldBrowser/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36" # Agent obsolète
    ]

    for i in range(num_records):
        user_id = random.choice(users)
        controller = random.choice(controllers)
        action = random.choice(actions.get(controller, ['View']))
        
        # Simuler des actions privilégiées pour certains utilisateurs
        if user_id == 'user_it_admin' and random.random() < 0.7: # 70% de chance d'action privilégiée
            controller = random.choice(['UserManagement', 'AdminPanel', 'SystemConfig'])
            action = random.choice(actions.get(controller, ['Access']))
        elif user_id == 'user_finance_01' and random.random() < 0.6: # 60% de chance d'action financière
            controller = random.choice(['Invoice', 'Payment'])
            action = random.choice(actions.get(controller, ['View']))
        elif user_id == 'user_external_auditor' and random.random() < 0.3: # Simuler un changement d'agent suspect
            user_agent = random.choice(user_agents) if random.random() < 0.9 else "MaliciousAgent/1.0 (Linux)"
        else:
            user_agent = random.choice(user_agents)

        action_time = start_date + timedelta(minutes=random.randint(1, 1440 * 30)) # Sur 30 jours
        duration = random.randint(1, 300) # Durée en secondes

        # Simuler des scénarios spécifiques pour les règles d'audit
        # Scénario PAM : Activité hors heures pour user_it_admin
        if user_id == 'user_it_admin' and random.random() < 0.05: # 5% de chance d'activité hors heures
            action_time = start_date + timedelta(minutes=random.randint(1, 1440 * 30))
            hour = random.choice(list(range(0, 8)) + list(range(19, 24))) # Heures hors bureau
            action_time = action_time.replace(hour=hour, minute=random.randint(0, 59))
            duration = random.randint(300, 1000) # Longue durée

        # Scénario SoD : user_finance_02 crée et approuve une facture
        if user_id == 'user_finance_02' and random.random() < 0.02: # 2% de chance de conflit SoD
            # Action 1: Créer facture
            data.append({
                'user_id': user_id,
                'controller': 'Invoice',
                'action': 'Create',
                'actionlog': f"{user_id};Invoice;Create;LogEntry",
                'actiontime': action_time.strftime('%Y-%m-%d %H:%M:%S'),
                'starttime': (action_time - timedelta(seconds=duration)).strftime('%Y-%m-%d %H:%M:%S'),
                'endtime': action_time.strftime('%Y-%m-%d %H:%M:%S'),
                'duration': duration,
                'useragent': user_agent
            })
            # Action 2: Approuver paiement (quelques minutes plus tard)
            action_time_2 = action_time + timedelta(minutes=random.randint(1, 5))
            data.append({
                'user_id': user_id,
                'controller': 'Payment',
                'action': 'Approve',
                'actionlog': f"{user_id};Payment;Approve;LogEntry",
                'actiontime': action_time_2.strftime('%Y-%m-%d %H:%M:%S'),
                'starttime': (action_time_2 - timedelta(seconds=random.randint(1, 100))).strftime('%Y-%m-%d %H:%M:%S'),
                'endtime': action_time_2.strftime('%Y-%m-%d %H:%M:%S'),
                'duration': random.randint(1, 100),
                'useragent': user_agent
            })
            continue # Passer à la prochaine itération pour ne pas ajouter la ligne principale

        data.append({
            'user_id': user_id,
            'controller': controller,
            'action': action,
            'actionlog': f"{user_id};{controller};{action};LogEntry", # Simule un champ actionlog
            'actiontime': action_time.strftime('%Y-%m-%d %H:%M:%S'),
            'starttime': (action_time - timedelta(seconds=duration)).strftime('%Y-%m-%d %H:%M:%S'),
            'endtime': action_time.strftime('%Y-%m-%d %H:%M:%S'),
            'duration': duration,
            'useragent': user_agent
        })
    
    df = pd.DataFrame(data)
    # Convertir la colonne 'actiontime' en datetime pour l'utiliser comme timestamp
    df['timestamp'] = pd.to_datetime(df['actiontime'])
    # Assurez-vous que 'duration' est numérique, gère les erreurs et remplace les NaN par 0
    df['duration'] = pd.to_numeric(df['duration'], errors='coerce').fillna(0)
    
    return df

# Génération du DataFrame
print("Génération du dataset synthétique...")
df = generate_synthetic_audit_data(num_records=2000) # Générer 2000 enregistrements
print("Dataset synthétique généré avec succès.")
print("\nPremières lignes du DataFrame généré:")
print(df.head())
print("\nNoms des colonnes du DataFrame généré:")
print(df.columns.tolist())


# --- 2. Moteur de Règles d'Audit ---

# Définition des règles pour PAM et SoD

# Règles PAM (Privileged Access Management)
# Pour cet exemple, nous allons considérer les actions sur 'UserManagement', 'AdminPanel', 'SystemConfig' comme privilégiées.
privileged_controllers = ['UserManagement', 'AdminPanel', 'SystemConfig']

def check_pam_violations(dataframe):
    pam_findings = []
    
    # Trouver les utilisateurs qui effectuent des actions privilégiées
    privileged_activities = dataframe[dataframe['controller'].isin(privileged_controllers)].copy()
    
    # Vérification 1 : Activité privilégiée en dehors des heures de bureau (ex: avant 8h ou après 18h)
    for index, row in privileged_activities.iterrows():
        hour = row['timestamp'].hour
        if not (8 <= hour <= 18): # Si l'heure est en dehors de 8h-18h
            pam_findings.append({
                'Type de Constat': 'PAM - Activité hors heures ouvrées',
                'Gravité': 'Moyenne',
                'Description': f"L'utilisateur '{row['user_id']}' a effectué une action privilégiée ('{row['action']}' sur '{row['controller']}') en dehors des heures de bureau à {row['timestamp']}.",
                'Utilisateur': row['user_id'],
                'Date': row['timestamp'].date()
            })
            
    # Vérification 2 : Comptes à privilèges "dormants" (pas d'activité récente)
    # Ici, nous allons identifier les utilisateurs qui ont des activités privilégiées mais très sporadiques sur la période d'audit.
    # On considère une activité sporadique si moins de 5 actions privilégiées sur la période totale
    user_activity_counts = privileged_activities.groupby('user_id').size().reset_index(name='activity_count')
    # S'assurer que 'user_it_admin' est un utilisateur privilégié pour le test
    all_privileged_users = dataframe[dataframe['controller'].isin(privileged_controllers)]['user_id'].unique()
    
    for user_id in all_privileged_users:
        if user_id not in user_activity_counts['user_id'].values:
            # L'utilisateur est considéré privilégié mais n'a eu aucune activité privilégiée
            pam_findings.append({
                'Type de Constat': 'PAM - Compte privilégié dormant (aucune activité)',
                'Gravité': 'Faible',
                'Description': f"Le compte privilégié '{user_id}' n'a effectué aucune activité privilégiée sur la période d'audit, ce qui pourrait indiquer un compte dormant ou sous-utilisé.",
                'Utilisateur': user_id
            })
        else:
            activity_count = user_activity_counts[user_activity_counts['user_id'] == user_id]['activity_count'].iloc[0]
            if activity_count < 5: # Moins de 5 activités privilégiées
                 pam_findings.append({
                    'Type de Constat': 'PAM - Activité privilégiée sporadique',
                    'Gravité': 'Faible',
                    'Description': f"L'utilisateur '{user_id}' a effectué un nombre très faible d'activités privilégiées ({activity_count}) sur la période, ce qui pourrait indiquer un compte dormant ou sous-utilisé.",
                    'Utilisateur': user_id
                })

    # Vérification 3 : Anomalies dans la durée des sessions privilégiées (par exemple, durée anormalement longue)
    if not privileged_activities.empty:
        # Filtrer les durées non nulles et non infinies pour le calcul
        valid_durations = privileged_activities['duration'].dropna()
        if not valid_durations.empty:
            mean_duration = valid_durations.mean()
            std_duration = valid_durations.std()
            
            if std_duration > 0: # Éviter la division par zéro si toutes les durées sont identiques
                long_duration_threshold = mean_duration + (3 * std_duration) # Plus de 3 écarts-types au-dessus de la moyenne
                anomalous_duration_activities = privileged_activities[privileged_activities['duration'] > long_duration_threshold]
                
                for index, row in anomalous_duration_activities.iterrows():
                    pam_findings.append({
                        'Type de Constat': 'PAM - Durée d\'activité privilégiée anormale',
                        'Gravité': 'Élevée',
                        'Description': f"L'utilisateur '{row['user_id']}' a effectué une action privilégiée ('{row['action']}' sur '{row['controller']}') avec une durée anormalement longue ({row['duration']}s) à {row['timestamp']}.",
                        'Utilisateur': row['user_id'],
                        'Date': row['timestamp'].date()
                    })

    # Vérification 4 : Changement d'agent utilisateur suspect pour un utilisateur privilégié
    for user_id in privileged_activities['user_id'].unique():
        user_privileged_logs = privileged_activities[privileged_activities['user_id'] == user_id].sort_values(by='timestamp')
        
        if len(user_privileged_logs) > 1:
            for i in range(len(user_privileged_logs) - 1):
                current_log = user_privileged_logs.iloc[i]
                next_log = user_privileged_logs.iloc[i+1]
                
                # Si le user_agent change radicalement en peu de temps (ex: moins de 5 minutes)
                # On compare les user_agents bruts pour la simulation
                if current_log['useragent'] != next_log['useragent'] and \
                   (next_log['timestamp'] - current_log['timestamp']) <= timedelta(minutes=5):
                    pam_findings.append({
                        'Type de Constat': 'PAM - Changement suspect d\'agent utilisateur',
                        'Gravité': 'Élevée',
                        'Description': f"L'utilisateur privilégié '{user_id}' a changé d'agent utilisateur de '{current_log['useragent']}' à '{next_log['useragent']}' en un court laps de temps ({next_log['timestamp'] - current_log['timestamp']}) lors d'actions privilégiées.",
                        'Utilisateur': user_id,
                        'Date': current_log['timestamp'].date()
                    })

    return pam_findings

# Règles SoD (Séparation des Tâches)
# Définir des paires ou des séquences d'actions conflictuelles plus complexes
sod_conflicts = [
    # Conflit 1 : Création de facture ET approbation de paiement par le même utilisateur
    {'actions': [
        {'controller': 'Invoice', 'action': 'Create'},
        {'controller': 'Payment', 'action': 'Approve'}
    ],
     'risk': 'Fraude - Création et approbation de paiement',
     'time_window_minutes': 60 # Fenêtre de temps pour détecter le conflit
    },
    # Conflit 2 : Modification des droits d'un utilisateur ET accès à un panneau d'administration par le même utilisateur
    {'actions': [
        {'controller': 'UserManagement', 'action': 'Edit_Permissions'},
        {'controller': 'AdminPanel', 'action': 'Access'}
    ],
     'risk': 'Abus de privilèges - Auto-attribution de droits',
     'time_window_minutes': 30
    },
    # Conflit 3 (plus complexe) : Création de fournisseur, Saisie de facture ET Exécution de paiement
    {'actions': [
        {'controller': 'Supplier', 'action': 'Create'},
        {'controller': 'Invoice', 'action': 'Enter'}, # Assuming 'Enter' is the action for 'Saisie'
        {'controller': 'Payment', 'action': 'Execute'}
    ],
     'risk': 'Fraude - Cycle complet fournisseur-paiement',
     'time_window_minutes': 120 # Fenêtre de temps plus large pour une séquence
    }
]

def check_sod_violations(dataframe):
    sod_findings = []
    
    for conflict_rule in sod_conflicts:
        num_actions_in_conflict = len(conflict_rule['actions'])
        
        # Filtrer toutes les actions pertinentes pour cette règle de conflit
        relevant_actions_filters = []
        for action_def in conflict_rule['actions']:
            relevant_actions_filters.append(
                (dataframe['controller'] == action_def['controller']) & 
                (dataframe['action'] == action_def['action'])
            )
        
        # Combiner les filtres
        # Assurez-vous que relevant_actions_filters n'est pas vide
        if not relevant_actions_filters:
            continue
            
        combined_filter = relevant_actions_filters[0]
        for i in range(1, len(relevant_actions_filters)):
            combined_filter = combined_filter | relevant_actions_filters[i]
            
        potential_violations = dataframe[combined_filter].sort_values(by='timestamp')
        
        # Regrouper par utilisateur pour vérifier les séquences
        for user_id, user_activities in potential_violations.groupby('user_id'):
            # Si l'utilisateur n'a pas assez d'activités pour former la séquence, passer
            if len(user_activities) < num_actions_in_conflict:
                continue

            # Vérifier toutes les combinaisons possibles de séquences d'actions
            for i in range(len(user_activities) - num_actions_in_conflict + 1):
                sequence = user_activities.iloc[i : i + num_actions_in_conflict]
                
                # Vérifier si toutes les actions de la règle sont présentes dans la séquence
                # et si elles sont dans l'ordre défini (ou si l'ordre n'est pas strict, juste la présence)
                # Pour la simplicité, nous vérifions juste la présence et la fenêtre de temps.
                # Une implémentation réelle vérifierait l'ordre exact si nécessaire.
                
                # Vérifier que toutes les actions de la règle sont dans la séquence
                all_actions_present = True
                actions_in_sequence_tuples = [] # Utiliser des tuples pour une comparaison facile
                for _, row in sequence.iterrows():
                    actions_in_sequence_tuples.append((row['controller'], row['action']))

                for required_action in conflict_rule['actions']:
                    if (required_action['controller'], required_action['action']) not in actions_in_sequence_tuples:
                        all_actions_present = False
                        break
                
                if all_actions_present:
                    first_action_time = sequence.iloc[0]['timestamp']
                    last_action_time = sequence.iloc[-1]['timestamp']
                    
                    if (last_action_time - first_action_time) <= timedelta(minutes=conflict_rule['time_window_minutes']):
                        # Correction de l'f-string ici
                        actions_str = ', '.join([f'{a["controller"]}/{a["action"]}' for a in conflict_rule['actions']])
                        sod_findings.append({
                            'Type de Constat': 'SoD - Conflit de séquence détecté',
                            'Gravité': 'Élevée',
                            'Description': f"L'utilisateur '{user_id}' a effectué une séquence d'actions conflictuelles ({actions_str}) dans une fenêtre de {conflict_rule['time_window_minutes']} minutes, ce qui constitue un conflit de Séparation des Tâches : {conflict_rule['risk']}.",
                            'Utilisateur': user_id,
                            'Actions Conflituelles': [f'{a["controller"]}/{a["action"]}' for a in conflict_rule['actions']],
                            'Période': f"{first_action_time} à {last_action_time}"
                        })
                        # Pour éviter les doublons si une séquence est un sous-ensemble d'une autre
                        # ou si des activités se chevauchent, on pourrait ajouter un mécanisme de déduplication
                        # ou ajuster la boucle pour avancer de 'num_actions_in_conflict'
                        
    return sod_findings


# --- 3. Exécution de l'Audit et Génération des Constats ---
print("\n--- Exécution de l'Audit ---")
pam_results = check_pam_violations(df)
sod_results = check_sod_violations(df)

print("\n--- Constats PAM ---")
if pam_results:
    for finding in pam_results:
        print(f"[{finding['Gravité']}] {finding['Description']}")
else:
    print("Aucun constat PAM majeur détecté dans cet échantillon.")

print("\n--- Constats SoD ---")
if sod_results:
    for finding in sod_results:
        print(f"[{finding['Gravité']}] {finding['Description']}")
else:
    print("Aucun conflit SoD détecté dans cet échantillon.")


# --- 4. Module de Recommandations (Conceptuel) ---
# Ce module lierait les constats à des recommandations prédéfinies.

def generate_recommendations(findings):
    recommendations = []
    for finding in findings:
        if "PAM - Activité hors heures ouvrées" in finding['Type de Constat']:
            recommendations.append(f"Pour le constat '{finding['Type de Constat']}' (Utilisateur: {finding['Utilisateur']}), il est recommandé de : "
                                   f"1. Mettre en place des plages horaires d'accès strictes pour les comptes à privilèges. "
                                   f"2. Implémenter une solution de Privileged Access Management (PAM) pour la gestion des sessions et la traçabilité en temps réel. "
                                   f"3. Revoir la politique d'authentification pour inclure la Multi-Factor Authentication (MFA) sur ces comptes, conformément à l'ISO 27001 (A.9.2.4) et aux exigences du RGPD (Article 32) pour la protection des données.")
        elif "PAM - Activité privilégiée sporadique" in finding['Type de Constat']:
            recommendations.append(f"Pour le constat '{finding['Type de Constat']}' (Utilisateur: {finding['Utilisateur']}), il est recommandé de : "
                                   f"1. Procéder à une revue des comptes à privilèges inactifs ou sous-utilisés. "
                                   f"2. Désactiver ou supprimer les comptes non nécessaires, conformément à l'ISO 27001 (A.9.2.1).")
        elif "PAM - Durée d'activité privilégiée anormale" in finding['Type de Constat']:
            recommendations.append(f"Pour le constat '{finding['Type de Constat']}' (Utilisateur: {finding['Utilisateur']}), il est recommandé de : "
                                   f"1. Mettre en place une surveillance en temps réel des sessions privilégiées pour détecter les durées anormales. "
                                   f"2. Investiguer les cas de sessions excessivement longues pour comprendre la cause et s'assurer de la légitimité de l'activité. "
                                   f"3. Renforcer les contrôles d'accès à distance et les mécanismes de déconnexion automatique.")
        elif "PAM - Changement suspect d'agent utilisateur" in finding['Type de Constat']:
            recommendations.append(f"Pour le constat '{finding['Type de Constat']}' (Utilisateur: {finding['Utilisateur']}), il est recommandé de : "
                                   f"1. Implémenter une surveillance des attributs de session (comme l'agent utilisateur, l'adresse IP source) pour les comptes privilégiés. "
                                   f"2. Mettre en place des alertes automatiques en cas de changement brusque de ces attributs. "
                                   f"3. Exiger une ré-authentification forte en cas de détection d'un comportement suspect, conformément aux principes de sécurité adaptative.")
        elif "SoD - Conflit de séquence détecté" in finding['Type de Constat']:
            recommendations.append(f"Pour le constat '{finding['Type de Constat']}' (Utilisateur: {finding['Utilisateur']}), il est recommandé de : "
                                   f"1. Réviser les rôles et permissions de l'utilisateur '{finding['Utilisateur']}' dans le système pour éliminer le cumul de fonctions conflictuelles. "
                                   f"2. Mettre en place une matrice de SoD claire et l'intégrer dans le processus d'attribution des rôles. "
                                   f"3. En l'absence de séparation stricte, implémenter des contrôles compensatoires efficaces (ex: revue et approbation par un tiers indépendant), en ligne avec le SOX (Section 404) et l'ISO 27001 (A.6.1.2). "
                                   f"4. Utiliser des outils d'analyse de SoD pour scanner régulièrement les droits et les activités.")
    return recommendations

print("\n--- Recommandations ---")
all_findings = pam_results + sod_results
recommendations_list = generate_recommendations(all_findings)
if recommendations_list:
    for rec in recommendations_list:
        print(f"- {rec}\n")
else:
    print("Aucune recommandation générée car aucun constat n'a été détecté.")
