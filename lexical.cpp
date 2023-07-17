#include <iostream>
#include <fstream>
#include <regex>
#include <set>

using namespace std;

// Function to identify keywords, identifiers, operators, and special characters
void analyze_c_program(const string& file_path) {
    set<string> keywords = {"auto", "break", "case", "char", "const", "continue", "default",
                            "do", "double", "else", "enum", "extern", "float", "for", "goto",
                            "if", "int", "long", "register", "return", "short", "signed", "sizeof",
                            "static", "struct", "switch", "typedef", "union", "unsigned", "void",
                            "volatile", "while"};

    set<string> identifiers;
    set<string> operators = {"+", "-", "*", "/", "%", "=", "==", "!=", "<", ">", "<=", ">=",
                             "&&", "||", "!", "++", "--", "+=", "-=", "*=", "/=", "%="};
    set<string> special_chars = {"(", ")", "{", "}", "[", "]", ",", ";"};

    ifstream file(file_path);
    if (!file.is_open()) {
        cerr << "Error opening file: " << file_path << endl;
        return;
    }

    string line;
    string content;
    while (getline(file, line)) {
        content += line + '\n';
    }
    file.close();

    // Remove comments from the code
    content = regex_replace(content, regex("/\\*.*?\\*/"), "");
    content = regex_replace(content, regex("//.*?\n"), "");

    // Tokenize the code
    regex word_regex("\\b\\w+\\b|[^\\s\\w]");
    auto words_begin = sregex_iterator(content.begin(), content.end(), word_regex);
    auto words_end = sregex_iterator();

    for (sregex_iterator it = words_begin; it != words_end; ++it) {
        string token = it->str();
        if (keywords.find(token) != keywords.end()) {
            // cout << "Keyword: " << token << endl;
            cout<<token<<"->keyword"<<endl;
        } else if (regex_match(token, regex("[a-zA-Z_]\\w*"))) {
            identifiers.insert(token);
            // cout << "Identifier: " << token << endl;
            cout<<token<<"->identifier"<<endl;
        } else if (operators.find(token) != operators.end()) {
            // cout << "Operator: " << token << endl;
            cout<<token<<"->operator"<<endl;
        } else if (special_chars.find(token) != special_chars.end()) {
            // cout << "Special Character: " << token << endl;
            cout<<token<<"->special character"<<endl;
        }
    }

    // cout << "\nIdentifiers:\n";
    // for (const string& identifier : identifiers) {
    //     cout << identifier << endl;
    // }
}

int main() {
    string file_path = "E:\\college\\coding\\programing\\Compiler_design\\test.txt";
    analyze_c_program(file_path);
    return 0;
}
