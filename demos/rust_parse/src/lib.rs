pub fn normalize_legal_text(input: &str) -> String {
    input
        .chars()
        .filter(|c| *c != '\u{0640}') // tatweel
        .collect()
}

pub fn preserve_char_offsets(input: &str) -> Vec<(usize, char)> {
    input.char_indices().collect()
}

// this lib.rs file only contains a sanitized/minimal version of the actual architecture, real implementation is private
