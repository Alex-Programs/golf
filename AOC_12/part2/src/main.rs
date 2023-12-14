use std::fs;

fn evaluate_if_valid(part: &str, contigs: &[usize]) -> bool {
    let mut contig_section_length = 0;
    let mut contig_sections = Vec::new();

    for ch in part.chars() {
        if ch == '#' {
            contig_section_length += 1;
        } else {
            if contig_section_length != 0 {
                contig_sections.push(contig_section_length);
                contig_section_length = 0;
            }
        }
    }

    if contig_section_length != 0 {
        contig_sections.push(contig_section_length);
    }

    contig_sections == contigs
}

fn make_all_possibilities(parts: Vec<char>) -> Vec<String> {
    let mut to_randomise_indexes = Vec::new();
    for (i, &part) in parts.iter().enumerate() {
        if part == '?' {
            to_randomise_indexes.push(i);
        }
    }

    println!("Getting upper bound");
    let upper_bound: u128 = 2u128.pow(to_randomise_indexes.len() as u32);
    println!("Upper bound: {}", upper_bound);
    let mut possibilities = Vec::new();

    for i in 0..upper_bound {
        let binary = format!("{:b}", i).chars().rev().collect::<String>();
        let mut possibility = parts.clone();

        for (j, binary_char) in binary.chars().enumerate() {
            possibility[to_randomise_indexes[j]] = if binary_char == '1' { '#' } else { '.' };
        }

        let combined = possibility.into_iter().collect();

        possibilities.push(combined);
    }

    possibilities
}

fn main() {
    let contents = fs::read_to_string("input.txt").expect("Failed to read file");
    let lines: Vec<&str> = contents.lines().collect();

    let mut total_valid = 0;

    for line in lines {
        let mut parts: Vec<char> = line.split_whitespace().next().unwrap().chars().collect();
        let contig: Vec<usize> = line.split_whitespace().nth(1).unwrap().split(',').map(|x| x.parse().unwrap()).collect();

        let mut out = Vec::new();
        for _ in 0..5 {
            out.extend_from_slice(&parts);
            out.push('?');
        }

        parts = out;

        let mut out = Vec::new();
        for _ in 0..5 {
            out.extend_from_slice(&parts);
        }

        parts = out;

        println!("{:?}", parts);
        let poss = make_all_possibilities(parts);
        let mut valid_count = 0;

        for p in poss {
            if evaluate_if_valid(&p, &contig) {
                valid_count += 1;
            }
        }

        println!("{}", valid_count);
        total_valid += valid_count;
    }

    println!("{}", total_valid);
}