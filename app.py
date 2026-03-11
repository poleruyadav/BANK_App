import streamlit as st

# Page settings
st.set_page_config(page_title="SBI Bank App", page_icon="🏦", layout="centered")

# Bank Class
class BankApplication:
    bank_name = "SBI"

    def __init__(self, name, account_number, age, mobile_number, balance):
        self.name = name
        self.account_number = account_number
        self.age = age
        self.mobile_number = mobile_number
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"✅ Transaction Successful. Collected ₹{amount}"
        else:
            return "❌ Insufficient Balance"

    def deposit(self, amount):
        self.balance += amount
        return f"✅ Deposit Successful. Total Balance: ₹{self.balance}"

    def update_mobile(self, new_number):
        self.mobile_number = new_number
        return f"📱 Mobile number updated: {self.mobile_number}"

    def check_balance(self):
        return f"💰 Total Account Balance: ₹{self.balance}"


# Title
st.markdown("<h1 style='text-align:center;color:green;'>🏦 SBI Bank Application</h1>", unsafe_allow_html=True)
st.write("---")

# Session storage
if "account" not in st.session_state:
    st.session_state.account = None


# Sidebar Menu
st.sidebar.title("Bank Menu")
menu = ["Create Account", "Deposit", "Withdraw", "Update Mobile", "Check Balance"]
choice = st.sidebar.radio("Select Option", menu)


# Sidebar Account Details
if st.session_state.account:
    st.sidebar.success("Account Active")
    st.sidebar.write("**Name:**", st.session_state.account.name)
    st.sidebar.write("**Account No:**", st.session_state.account.account_number)


# Create Account
if choice == "Create Account":

    st.subheader("📝 Create New Account")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Enter Name")
        age = st.number_input("Age", min_value=18)

    with col2:
        account_number = st.text_input("Account Number")
        mobile = st.text_input("Mobile Number")

    balance = st.number_input("Initial Balance", min_value=0)

    if st.button("Create Account", use_container_width=True):
        st.session_state.account = BankApplication(name, account_number, age, mobile, balance)
        st.success("🎉 Account Created Successfully!")


# Deposit
elif choice == "Deposit":

    st.subheader("💵 Deposit Money")

    if st.session_state.account:

        amount = st.number_input("Enter Deposit Amount", min_value=1)

        if st.button("Deposit", use_container_width=True):
            result = st.session_state.account.deposit(amount)
            st.success(result)

    else:
        st.warning("⚠ Please create an account first")


# Withdraw
elif choice == "Withdraw":

    st.subheader("💳 Withdraw Money")

    if st.session_state.account:

        amount = st.number_input("Enter Withdraw Amount", min_value=1)

        if st.button("Withdraw", use_container_width=True):
            result = st.session_state.account.withdraw(amount)
            if "Successful" in result:
                st.success(result)
            else:
                st.error(result)

    else:
        st.warning("⚠ Please create an account first")


# Update Mobile
elif choice == "Update Mobile":

    st.subheader("📱 Update Mobile Number")

    if st.session_state.account:

        new_mobile = st.text_input("Enter New Mobile Number")

        if st.button("Update Number", use_container_width=True):
            result = st.session_state.account.update_mobile(new_mobile)
            st.success(result)

    else:
        st.warning("⚠ Please create an account first")


# Check Balance
elif choice == "Check Balance":

    st.subheader("💰 Account Balance")

    if st.session_state.account:
        result = st.session_state.account.check_balance()

        st.info(result)

        st.metric("Current Balance", f"₹{st.session_state.account.balance}")

    else:
        st.warning("⚠ Please create an account first")