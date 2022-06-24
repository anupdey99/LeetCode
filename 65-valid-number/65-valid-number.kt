class Solution {
    fun isNumber(s: String): Boolean {
        if (s.trim().isEmpty()) return false
        return s.matches(Regex("^[+-]?(\\d+[.]?\\d*|[.]\\d+)([eE][+-]?\\d+)?$"))
    }
}