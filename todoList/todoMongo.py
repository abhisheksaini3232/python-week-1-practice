import pymongo

# Your Atlas connection string
connectionString = "mongodb+srv://manojsaini653733_db_user:7mUuKvsYRBkRICcF@cluster0.noljb9f.mongodb.net/?retryWrites=true&w=majority"

if __name__ == '__main__':  # Correct condition for direct execution
    client = pymongo.MongoClient(connectionString)
    
    try:
        # Test connection
        client.admin.command('ping')
        print("✅ Connected to MongoDB Atlas!")
        
        # YOUR DB: projects, YOUR Collection: todoList
        db = client['projects']      # Database name
        todos = db['todoList']       # Collection name
        
        # Insert test todo
        todo_id = todos.insert_one({
            "title": "Buy milk", 
            "done": False, 
            "created_at": "2025-12-27"
        }).inserted_id
        
        print(f"✅ Inserted todo with ID: {todo_id}")
        print(f"✅ Check your Atlas dashboard: projects.todoList")
        
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        client.close()
