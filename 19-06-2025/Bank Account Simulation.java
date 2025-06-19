

class BankAccount {
    int balance = 1000;

    void deposit(int amount) {
        balance += amount;
        System.out.println("Deposited: " + amount);
    }

    void withdraw(int amount) {
        if (amount > balance)
            System.out.println("Insufficient balance.");
        else {
            balance -= amount;
            System.out.println("Withdrawn: " + amount);
        }
    }

    void checkBalance() {
        System.out.println("Balance: " + balance);
    }

    public static void main(String[] args) {
        BankAccount acc = new BankAccount();
        acc.deposit(500);
        acc.withdraw(300);
        acc.checkBalance();
    }
}
