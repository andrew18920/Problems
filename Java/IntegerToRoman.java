class IntegerToRoman {
    public String intToRoman(int num) {
        int[] values = { 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 };
        String[] letters = { "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" };

        StringBuilder output = new StringBuilder();
        for (int i = 0; i < values.length; i++) {
            while (num >= values[i]) {
                output.append(letters[i]);
                num -= values[i];
            }
        }

        return output.toString();
    }

    public static void main(String[] args) {
        IntegerToRoman solve = new IntegerToRoman();
        String[] solutions = {
                String.format("solve.intToRoman(1234) = '%s'", solve.intToRoman(1234)),
                String.format("solve.intToRoman(1234) = '%s'", solve.intToRoman(12)),
                String.format("solve.intToRoman(1234) = '%s'", solve.intToRoman(0)),
                String.format("solve.intToRoman(1234) = '%s'", solve.intToRoman(1927)),
                String.format("solve.intToRoman(1234) = '%s'", solve.intToRoman(3049)),
        };

        for (String solution : solutions) {
            System.out.println(solution);
        }
    }
}