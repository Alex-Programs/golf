fn main() {
    let data = std::fs::read_to_string("../input.txt").expect("Unable to read file");

    let start_time = std::time::Instant::now();

    let numbers_lookup = vec![
            ("one", '1'),
            ("two", '2'),
            ("three", '3'),
            ("four", '4'),
            ("five", '5'),
            ("six", '6'),
            ("seven", '7'),
            ("eight", '8'),
            ("nine", '9')
    ];

    let mut nums = Vec::with_capacity(10);
    let lines = data.split("\n").collect::<Vec<&str>>();

    let mut string_start_index = 0;
    let mut string_end_index = 0;
    let mut sum: u32 = 0;

    for _ in 0..1000 {
        for line in &lines {
            nums.clear();
            string_start_index = 0;
            string_end_index = 0;
            
            for c in line.chars() {
                string_end_index += 1;
                if c.is_numeric() {
                    string_start_index = string_end_index;
                    nums.push(c);
                } else {
                    let substring = &line[string_start_index..string_end_index];
                    for (word, num) in &numbers_lookup {
                        if substring.contains(word) {
                            nums.push(*num);
                            string_start_index = string_end_index - 1;
                        }
                    }
                }
            }
    
            let first = nums[0];
            let last = nums[nums.len() - 1];
    
            let combined = format!("{}{}", first, last);
            let combined_int = combined.parse::<u32>().unwrap();
            sum += combined_int;
        }
    }
    let end_time = std::time::Instant::now();
    let duration = end_time.duration_since(start_time) / 1000;

    println!("Duration: {:?}", duration);
}