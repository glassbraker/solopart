import json
import requests
import csv

import os

if not os.path.exists("data"):
 os.makedirs("data")

# GitHub Authentication function
def github_auth(url, lsttoken, ct):
    jsonData = None
    try:
        ct = ct % len(lstTokens)
        headers = {'Authorization': 'Bearer {}'.format(lsttoken[ct])}
        request = requests.get(url, headers=headers)
        jsonData = json.loads(request.content)
        ct += 1
    except Exception as e:
        pass
        print(e)
    return jsonData, ct

# @dictFiles, empty dictionary of files
# @lstTokens, GitHub authentication tokens
# @repo, GitHub repo
def countfiles(dictfiles, lsttokens, repo):
    ipage = 1  # url page counter
    ct = 0  # token counter

    try:
        # loop though all the commit pages until the last returned empty page
        while True:
            spage = str(ipage)
            commitsUrl = 'https://api.github.com/repos/' + repo + '/commits?page=' + spage + '&per_page=100'
            jsonCommits, ct = github_auth(commitsUrl, lsttokens, ct) # jsonData

            #******************************************************************************************************edits
            #print(jsonCommits)
            #break
            #***********************************************************************************************end of edits


            # break out of the while loop if there are no more commits in the pages
            if len(jsonCommits) == 0:
                break
            # iterate through the list of commits in  spage yellow green
            
            '''
            [{'sha': 'eff976a9eec1706957b2fa594672105fa9c3fa1e', 'node_id': 'C_kwDOAj9xqNoAKGVmZjk3NmE5ZWVjMTcwNjk1N2IyZmE1OTQ2NzIxMDVmYTljM2ZhMWU', 'commit': {'author': {'name': 'Niall Scott', 'email': 'riverniall@gmail.com', 'date': '2024-10-04T07:42:57Z'}, 'committer': {'name': 'GitHub', 'email': 'noreply@github.com', 'date': '2024-10-04T07:42:57Z'}, 'message': "Optimise Gradle setting and script configuration (#238)\n\n* Tidied Gradle scripts so that common properties and logic are centralised in the root project's Gradle file. This prevents duplication of properties and logic in subprojects. Also updated Gradle, AGP and removed Proguard files which had no meaningful content.\r\n* Turn on Gradle configuration and build cache for speedy developer builds. Tidied up the root gradle.properties file a little.", 'tree': {'sha': '79d8fcc4d7bf106e7d3a6f020c950039b5810ae6', 'url': 'https://api.github.com/repos/scottyab/rootbeer/git/trees/79d8fcc4d7bf106e7d3a6f020c950039b5810ae6'}, 'url': 'https://api.github.com/repos/scottyab/rootbeer/git/commits/eff976a9eec1706957b2fa594672105fa9c3fa1e', 'comment_count': 0, 'verification': {'verified': True, 'reason': 'valid', 'signature': '-----BEGIN PGP SIGNATURE-----\n\nwsFcBAABCAAQBQJm/5yBCRC1aQ7uu5UhlAAAv6MQAJQ7c/y+BiFJ7qfRkw2bYVq8\nymvQPL4VVclK5qQLFIeg7GHSGRZDOiSbUXs2ikDQNy1MMl8vAoi/M2xntGiW+YG0\n3zgZHt6GozkICE/4uKp1rt3wEQS0cAgTHMCFTeijkQgY4Ly/tT3gYPbIyN48bCH0\ng+7eJLNwxjBOiWLDNcILBveUxTwdcUZSf2TKkAP5Ggvi/OAufEM6tkl8MxqP+vlS\nm4bJxlfm/qNdPAauKbYnErnPTyLNFK9Qs4ECL9gTlHcI7IBMDDRlWfmOXgdxm6AT\nn7GiXfF9Re7ez72+29REngmQu6n+WyV4Is7lUWhwtipyPkTRKttzg82KerawXjP6\nDz1nZSxS7yvmC3AxA93TEQKwLlkIhIxHmVNwE3G4ZxfQfiVwh9zCODwTXUDgIB2t\n2bRqWK6FabLT6SsWvLzw9FQFhHLCNbnMekNlJzi9noThsNC/G/09moMjQLppPusT\nYa+gJtcT2+KyO0MnwzambM7dmcUilkex6MgoNe6l4SE6jTt7fb1UtfBI/gKOmFEO\nLDrPtEMsD2IPepYxtkSWGnPcv8RiYBd743AMa9AlcfR7XmnqiWfsjc9CNnlYyiLt\nPkvjRquPEOy4gglt/7lQPQXZbxHHsxFBRsm2Tfr6Xqz//s+b0cG1IMjaymGRWCTJ\nPNOAfSdF6QBXzAIIlLjV\n=ZQ0a\n-----END PGP SIGNATURE-----\n', 'payload': "tree 79d8fcc4d7bf106e7d3a6f020c950039b5810ae6\nparent 8e8bc3c6a4494da20259b86f4e3c45ca8131241a\nauthor Niall Scott <riverniall@gmail.com> 1728027777 +0100\ncommitter GitHub <noreply@github.com> 1728027777 +0100\n\nOptimise Gradle setting and script configuration (#238)\n\n* Tidied Gradle scripts so that common properties and logic are centralised in the root project's Gradle file. This prevents duplication of properties and logic in subprojects. Also updated Gradle, AGP and removed Proguard files which had no meaningful content.\r\n* Turn on Gradle configuration and build cache for speedy developer builds. Tidied up the root gradle.properties file a little.", 'verified_at': '2024-11-05T06:09:13Z'}}, 'url': 'https://api.github.com/repos/scottyab/rootbeer/commits/eff976a9eec1706957b2fa594672105fa9c3fa1e', 'html_url': 'https://github.com/scottyab/rootbeer/commit/eff976a9eec1706957b2fa594672105fa9c3fa1e', 'comments_url': 'https://api.github.com/repos/scottyab/rootbeer/commits/eff976a9eec1706957b2fa594672105fa9c3fa1e/comments', 'author': {'login': 'NiallScott', 'id': 2347017, 'node_id': 'MDQ6VXNlcjIzNDcwMTc=', 'avatar_url': 'https://avatars.githubusercontent.com/u/2347017?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/NiallScott', 'html_url': 'https://github.com/NiallScott', 'followers_url': 'https://api.github.com/users/NiallScott/followers', 'following_url': 'https://api.github.com/users/NiallScott/following{/other_user}', 'gists_url': 'https://api.github.com/users/NiallScott/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/NiallScott/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/NiallScott/subscriptions', 'organizations_url': 'https://api.github.com/users/NiallScott/orgs', 'repos_url': 'https://api.github.com/users/NiallScott/repos', 'events_url': 'https://api.github.com/users/NiallScott/events{/privacy}', 'received_events_url': 'https://api.github.com/users/NiallScott/received_events', 'type': 'User', 'user_view_type': 'public', 'site_admin': False}, 'committer': {'login': 'web-flow', 'id': 19864447, 'node_id': 'MDQ6VXNlcjE5ODY0NDQ3', 'avatar_url': 'https://avatars.githubusercontent.com/u/19864447?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/web-flow', 'html_url': 'https://github.com/web-flow', 'followers_url': 'https://api.github.com/users/web-flow/followers', 'following_url': 'https://api.github.com/users/web-flow/following{/other_user}', 'gists_url': 'https://api.github.com/users/web-flow/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/web-flow/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/web-flow/subscriptions', 'organizations_url': 'https://api.github.com/users/web-flow/orgs', 'repos_url': 'https://api.github.com/users/web-flow/repos', 'events_url': 'https://api.github.com/users/web-flow/events{/privacy}', 'received_events_url': 'https://api.github.com/users/web-flow/received_events', 'type': 'User', 'user_view_type': 'public', 'site_admin': False}, 'parents': [{'sha': '8e8bc3c6a4494da20259b86f4e3c45ca8131241a', 'url': 'https://api.github.com/repos/scottyab/rootbeer/commits/8e8bc3c6a4494da20259b86f4e3c45ca8131241a', 'html_url': 'https://github.com/scottyab/rootbeer/commit/8e8bc3c6a4494da20259b86f4e3c45ca8131241a'}]},
            '''
            '''
            below grabs the commit, then gerambs al files that were changed in the commit, i need to grab the author the time and files, and save them in a packet...
            '''
            for shaObject in jsonCommits:
                sha = shaObject['sha']
                # For each commit, use the GitHub commit API to extract the files touched by the commit
                shaUrl = 'https://api.github.com/repos/' + repo + '/commits/' + sha
                shaDetails, ct = github_auth(shaUrl, lsttokens, ct)
                #nname = filenameObj['name']
                #print(shaDetails['commit'])
                holder = shaDetails['commit'] #GOTTA DIG THROUGH THOSE BRACKETS!!!
                holder2 = holder['author']
                #print(holder2)
                nname = holder2['name']
                touched = holder2['date']
                #print(nname)
                #print(touched)
                #touched = filenameObj['date']
                filesjson = shaDetails['files']
                #print(shaDetails)
                #break
                # adata.append([name, file name, touched])
                for filenameObj in filesjson:
                    filename = filenameObj['filename']
                    dictfiles[filename] = dictfiles.get(filename, 0) + 1
                    print(filename)
                    adata.append([nname, filename, touched])
            ipage += 1
            #******************************************************************************************************edits
            #print(jsonCommits)
            #break
            #***********************************************************************************************end of edits
    except:
        print("Error receiving data")
        exit(0)

# GitHub repo
repo = 'scottyab/rootbeer'
# repo = 'Skyscanner/backpack' # This repo is commit heavy. It takes long to finish executing
# repo = 'k9mail/k-9' # This repo is commit heavy. It takes long to finish executing
# repo = 'mendhak/gpslogger'


# put your tokens here
# Remember to empty the list when going to commit to GitHub.
# Otherwise they will all be reverted and you will have to re-create them
# I would advise to create more than one token for repos with heavy commits
lstTokens = ["faketoken"]

dictfiles = dict()
adata = []
countfiles(dictfiles, lstTokens, repo)
otherfiles = dictfiles.copy()  

for ffile, value in otherfiles.items(): #if i try and do this on the raw file it errors out
    if value >= 3: #if not touched again assume not source
        del dictfiles[ffile]
        llength = len(adata) #gotta check the length as array shrinks
        while(llength > 0):
            if adata[(llength -1)][1] == ffile:
                del adata[(llength -1)]
                #print (ffile + "removed \n")
            llength = llength - 1

print('Total number of source files: ' + str(len(dictfiles)))
#print (dictfiles)
file = repo.split('/')[1]
# change this to the path of your file
fileOutput = 'data/file_' + file + '_trimmed.csv'
rows = ["Filename", "Touches"]
fileCSV = open(fileOutput, 'w')
writer = csv.writer(fileCSV)
writer.writerow(rows)

#print(adata)

bigcount = None
bigfilename = None
for filename, count in dictfiles.items():
    rows = [filename, count]
    writer.writerow(rows)
    if bigcount is None or count > bigcount:
        bigcount = count
        bigfilename = filename
fileCSV.close()

#[nname, filename, touched]
fileOutput = 'data/file_graphdata.csv'
rows = ["Author", "Filename", "Touched on", str(len(dictfiles)) ]
fileCSV = open(fileOutput, 'w')
writer = csv.writer(fileCSV)
writer.writerow(rows)


#the resons i love arrays, I CAN USE NUMBERS :D

llength = len(adata)

while(llength > 0):
	rows = [adata[(llength -1)][0], adata[(llength -1)][1],adata[(llength -1)][2]] #yes this wrights the data in reverse, but the graph dont care
	writer.writerow(rows)
	llength = llength - 1
fileCSV.close()


print('The file ' + bigfilename + ' has been touched ' + str(bigcount) + ' times.')
