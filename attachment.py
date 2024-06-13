import ezgmail


# This is a thread that i have created.


def attachmentdownload(resulthreads):
    countofresults = len(resulthreads)
    try:
        for i in range(countofresults):
            if len(resulthreads[i].messages) > 1:
                for j in range(len(resulthreads[i].messages)):
                    resulthreads[i].messages[j].downloadAllAttachments()  # downloads attachment(s) for individual messages
            else:
                resulthreads[i].messages[0].downloadAllAttachments()
        print("Download compelete. Please check your root directory.")
    except:
        raise Exception("Error occured while downloading attachment(s).")



# This block of code doesnt run if we try to import it to another script.

if __name__ == '__main__':

    # query is the same string that you type on the gmail search box.
    query = input("Enter search query: ")

    # appending to make sure the result threads always has an attachment
    newquery = query + " + has:attachment"

    resulthreads = ezgmail.search(newquery)

    if len(resulthreads) == 0:
        print("Result has no attachments:")
    else:
        print("Result(s) with attachments:")
        for threads in resulthreads:
            print(f"Email Subject: {threads.messages[0].subject}")
        try:
            ask = input(
                "Do you want to download attachment(s) in result(s) (Yes/No)? ")  # Allows user to decide whether they want to download attachment(s) or not
            if ask == "Yes":
                attachmentdownload(resulthreads)
            else:
                print("Program exited")
        except:
            print("Something went wrong")
