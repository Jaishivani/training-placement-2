
class Student {
    String name;
    int[] marks = new int[3];

    Student(String name, int m1, int m2, int m3) {
        this.name = name;
        marks[0] = m1;
        marks[1] = m2;
        marks[2] = m3;
    }

    void displayGrade() {
        int sum = 0;
        for (int mark : marks) sum += mark;
        double avg = sum / 3.0;
        System.out.println("Student: " + name);
        System.out.println("Average: " + avg);
        if (avg >= 90) System.out.println("Grade: A");
        else if (avg >= 75) System.out.println("Grade: B");
        else if (avg >= 60) System.out.println("Grade: C");
        else System.out.println("Grade: F");
    }
    
    public static void main(String[] args) {
        Student s = new Student("John", 85, 78, 90);
        s.displayGrade();
    }
}
