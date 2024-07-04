class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> ans = new ArrayList<>();
        int i = 0;
        while (i < words.length) {
            StringBuilder sb = new StringBuilder();
            while (i < words.length && sb.length() + words[i].length() <= maxWidth) {
                sb.append(words[i]).append(" ");
                i++;
            }
            String str = sb.toString().trim();
            if (i < words.length)
                ans.add(addSpaces(str, maxWidth));
            else {
                while (str.length() != maxWidth)
                    str += " ";
                ans.add(str);
            }
        }
        return ans;
    }

    private String addSpaces(String s, int width) {
        StringBuilder sb = new StringBuilder();
        String[] arr = s.split(" ");
        int count = arr.length - 1;

        if (count == 0) {
            while (s.length() != width)
                s += " ";
            return s;
        }

        int padding = width - s.length();
        int equalSpace = padding / count;
        int moreNeeded = padding % count;
        String spaces = " ";

        while (equalSpace-- > 0)
            spaces += " ";

        String sp = spaces + " ";
        for (String ele : arr) {
            if (moreNeeded-- > 0)
                sb.append(ele + sp);
            else
                sb.append(ele + spaces);
        }
        return sb.toString().trim();
    }
}