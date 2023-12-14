use rand::thread_rng;
use rand::Rng;

fn quicksort(items: &mut [u32], start: usize, end: usize) {
    //println!("Data: {:?}, start: {}, end: {}", items, start, end);

    if start >= end {
        return;
    }
    
    let pivot = items[start];
    let mut left_pt = start + 1;
    let mut right_pt = end;

    loop {
        while left_pt <= right_pt && items[left_pt] <= pivot {
            left_pt += 1;
        }

        while right_pt >= left_pt && items[right_pt] >= pivot {
            right_pt -= 1;
        }

        if left_pt < right_pt {
            items.swap(left_pt, right_pt);
        } else {
            break;
        }
    }

    items.swap(start, right_pt);

    if right_pt > 0 {
        quicksort(items, start, right_pt - 1);
    }
    
    if right_pt < end {
        quicksort(items, right_pt + 1, end);
    }
}

fn main() {
    let mut random_vals = rand::thread_rng()
        .sample_iter(rand::distributions::Uniform::new(0, 100_000))
        .take(1_000_000)
        .collect::<Vec<u32>>();

    let length = random_vals.len();

    let start_time = std::time::Instant::now();

    quicksort(&mut random_vals, 0, length - 1);

    let elapsed_time = start_time.elapsed();

    println!("Elapsed time: {:?}", elapsed_time);

    // Double check that the array is sorted
    for i in 0..length - 1 {
        assert!(random_vals[i] <= random_vals[i + 1]);
    }
}
