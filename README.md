# 🚀 Onboarding - TukTuk's Journey

Welcome to the **TukTuk's Journey** repository! This guide will help you import the project into your local IDE and set it up correctly.

## 📥 1. Clone the Repository
Open your terminal or command prompt and run:

```sh
# Navigate to the folder where you want to clone the project
cd path/to/your/folder

# Clone the repository
git clone https://github.com/mateusoviana/TukTuk-s-Journey.git

# Enter the project folder
cd TukTuk-s-Journey
```

## 🛠 2. Open the Project in Your IDE
### **PyCharm**:
1. Open **PyCharm**.
2. Click **Open** and select the `TukTuk-s-Journey` folder.
3. Wait for PyCharm to load the project.
4. If prompted, accept the suggestion to create a virtual environment.

### **VS Code**:
1. Open **VS Code**.
2. Press `Ctrl + Shift + P`, type **"Open Folder"**, and select `TukTuk-s-Journey`.
3. Install recommended extensions if necessary.

## 🔧 3. Create and Activate a Virtual Environment (Optional but Recommended)

To ensure dependencies are managed correctly:

```sh
# Create a virtual environment (Windows)
python -m venv .venv

# Activate the virtual environment
# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

## 📦 4. Install Dependencies
With the virtual environment activated, install the required dependencies:

```sh
pip install pygame pytmx
```

Or just add them directly from your IDE.

## ▶️ 5. Run the Project
After installing the dependencies, you can run the project with:

```sh
python main.py  # Replace 'main.py' with the project's entry file
```

## 🗺 6. Setting Up Tiled and Using Existing Maps
The project includes **Tiled** map files that need to be opened and edited using the **Tiled Map Editor**.

### **Installing Tiled**
1. Download **Tiled** from the official website: [https://www.mapeditor.org/](https://www.mapeditor.org/).
2. Install it following the instructions for your operating system.
3. Open **Tiled** after installation.

### **Opening and Editing Existing Maps**
1. Inside **Tiled**, click **File > Open**.
2. Navigate to the project folder and open the `.tmx` map files located in the appropriate directory.
3. Edit the map as needed, making sure to save your changes.

### **Exporting Maps**
If required, you can export the maps in a different format:
1. Click **File > Export As...**.
2. Choose the format (e.g., JSON, PNG, etc.) and save it in the project's designated folder.

## 📝 7. Contributing
If you want to contribute to the project:
1. Create a branch for your feature/fix:
   ```sh
   git checkout -b my-feature
   ```
2. Make changes and commit:
   ```sh
   git add .
   git commit -m "My contribution"
   ```
3. Push to the repository:
   ```sh
   git push origin my-feature
   ```
4. Open a **Pull Request** on GitHub.

---
Congratulations! You are now ready to contribute to **TukTuk's Journey**. 🚀
Teste pomba

