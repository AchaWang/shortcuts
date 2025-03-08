if __name__=='__main__':
    with open("yt.lock", "w") as file:
        file.write("yt_dlp mission lock\n")
    print("Lock created successfully")