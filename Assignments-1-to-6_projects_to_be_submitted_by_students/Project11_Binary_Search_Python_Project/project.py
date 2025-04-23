def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1
    steps = 0  # 🧮 Track how many steps it took

    while low <= high:
        steps += 1
        mid = (low + high) // 2
        guess = sorted_list[mid]

        print(f"🔍 Step {steps}: Trying index {mid} -> {guess}")

        if guess == target:
            return mid  # 🎯 Found!
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # ❌ Not found


def main():
    print("📚 Welcome to the Binary Search Project!")

    # Input sorted list
    try:
        user_input = input("🔢 Enter sorted numbers separated by spaces: ")
        sorted_list = list(map(int, user_input.split()))
    except ValueError:
        print("⚠️ Please enter valid integers!")
        return

    target = int(input("🎯 Enter the number to search: "))

    # Perform Binary Search
    result = binary_search(sorted_list, target)

    # Show result
    if result != -1:
        print(f"✅ Number found at index {result}")
    else:
        print("❌ Number not found in the list.")


if __name__ == "__main__":
    main()
