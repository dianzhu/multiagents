# LLM Multi-Agents software:

1. Set up Microsoft's AutoGen framework on CMD:
   
   pip install pyautogen

2. Download and install Ollama on computer:
   
   https://ollama.com/

3. Download Meta's Llama 3.2 model and run model with Ollama on CMD:
   
   ollama run llama3.2

4. Set up MySQL with username and password, then create database called mydb in MySQL:
   
   CREATE DATABSE mydb

   The database.py file contains
   my MySQL username and password, you need to change your MySQL username and password in the file database.py

5. run code to compile result on CMD:
   
   python app.py

6. The four agents in the LLM multi-agents system will interact with each other for spam email dataset and output result. They will detect if each email is spam or not spam.

7. There are 102 emails. The four agents in the LLM multi-agents system are designed to read six emails contents at each time. If four agents finish completing 
   tasks for first six emails, the user will be asked to input question. The user can input "exit" and then four agents will continue interacting with each other for next 
   six emails. The user can continue inputting "exit" until four agents complete tasks for all 102 emails and the multi-agents system also stop running.

 
