use std::env;
use std::fs;
fn handle_input() -> String {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        eprintln!("Usage: {} <input_file>", args[0]);
        std::process::exit(1);
    }
    let filename = &args[1];
    // Get path to file, it is 2 levels above
    let filename_path = format!("{}", filename);
    dbg!(&filename_path);
    let input = fs::read_to_string(filename_path).expect("Failed to read the file");
    dbg!(&input);
    return input;
}
fn main() {
    println!("Hello, part1!");
    let input = handle_input();
    solution(&input);
}

fn solution(input: &str) -> String {
    let _ = input;
    "todo!()".to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() {
        assert_eq!(1, 1);
    }
}
