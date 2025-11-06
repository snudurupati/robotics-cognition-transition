#pragma once
#include <string>
#include <vector>
#include <optional>
struct CsvRow { std::vector<std::optional<std::string>> fields; };
class CsvParser {
public:
    explicit CsvParser(char delimiter = ',');
    std::vector<CsvRow> parse(const std::string& text) const;
private:
    char delim_;
};
