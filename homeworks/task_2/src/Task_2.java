public class Task_2 implements Task_2_base {
    @Override
    public int subtask_1_while(int num) {
        // Найти максимальное число, являющееся полным квадратом,
        // не превосходящее заданное натуральное num
        int FirstNumber = 0, LastNumber = 0;
        while (FirstNumber <= num){
            if(FirstNumber*FirstNumber <= num)
                LastNumber = FirstNumber*FirstNumber;
            else
                break;
            FirstNumber++;
        }
        return LastNumber;
    }

    @Override
    public int subtask_2_while(int num) {
        // Последовательность целых чисел p(n) определяется следующим образом:
        // p(0) = 1
        // p(k) = 2 * p(k - 1) + 6, k > 0
        //Найти элемент последовательности с номером num

        int FirstNumber = 1, PrevElement = 1, NextElement = 0;
        if(num == 0)
            return 1;
        else {
            while (FirstNumber <= num){
                NextElement = 2*PrevElement + 6;
                FirstNumber++;
                PrevElement = NextElement;
            }
            return NextElement;
        }
    }

    @Override
    public boolean subtask_3_while(int num, int base) {
        // Проверить, является ли число num натуральной степенью числа base
        int power = base;
        while(power < num) {
            power *= base;
        } return num==power;
    }

    @Override
    public int subtask_4_while(int start, int end) {
        // Вычислить, за какое минимальное число операций
        // вычесть 1
        // поделить на 2
        // число start можно превратить в end. Гарантируется, что start >= end >= 1
        int count = 0;
        while (start>end) {
            if(start%2 != 0 || start-end <= 2) {
                start -= 1;
                count++;
            } else {
                start /= 2;
                count++;
            }
        } return count;
    }
}
