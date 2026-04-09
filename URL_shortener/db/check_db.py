import sqlite3,os

def view_data():
    conn = sqlite3.connect('shortener.db')
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM urls")
        rows = cursor.fetchall()

        print(f"\n{'ID':<5} | {'Short Code':<12} | {'Clicks':<8} | {'Original URL'}")
        print("-" * 70)

        for row in rows:
            # Convert every item to a string first to avoid NoneType errors
            id_val = str(row[0])
            code_val = str(row[2]) if row[2] is not None else "N/A"
            clicks_val = str(row[3])
            url_val = str(row[1])

            print(f"{id_val:<5} | {code_val:<12} | {clicks_val:<8} | {url_val}")
        print("-" * 70 + "\n")

    except sqlite3.OperationalError:
        print("Error: The 'urls' table doesn't exist yet.")
    finally:
        conn.close()

def clean_database():
    db_file = 'shortener.db'
    
    if os.path.exists(db_file):
        try:
            # This completely deletes the file from your computer
            os.remove(db_file)
            print(f"\nSuccess: '{db_file}' has been deleted. All data is gone.")
            print("The API will create a brand new, empty database on the next request.\n")
        except PermissionError:
            print("\nError: Could not delete the database. Is the FastAPI server still running?")
            print("Please stop the uvicorn server and try again.\n")
    else:
        print(f"\nNo database file named '{db_file}' exists to wipe.\n")

if __name__ == "__main__":
    ask = """
    Do you want to view the database? (v): 
    Do you want to wipe all links? (w): 
    """

    confirm = input(ask)
    if confirm.lower() == 'v':
        view_data()
    elif confirm.lower() == 'w':
        confirm = input("Are you sure you want to wipe all links? (y/n): ")
        if confirm.lower() == 'y':
            clean_database()
        else:
            print("Operation cancelled.")
    else:
        print("Invalid input. Please try again.")