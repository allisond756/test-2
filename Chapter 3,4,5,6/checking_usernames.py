current_users=['amy123','jackact','buffalogirl','starboy','milk76']

new_users=['candycane45','suziepop','amy123','cowfriend','starboy']

for new_user in new_users:
    if new_user in current_users:
        print('Username already exists.')
    else:
        print('Username is available.')