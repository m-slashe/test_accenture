def print_multiples():
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print(f'Number: {i}, (multiple of 3 and 5)')
        elif i % 3 == 0:
            print(f'Number: {i}, (multiple of 3)')
        elif i % 5 == 0:
            print(f'Number: {i}, (multiple of 5)')


def verify_polindrome(string: str):
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


def compare_versions(version1: str, version2: str):
    version1_numbers = version1.split('.')
    version2_numbers = version2.split('.')
    max_range = max(len(version1_numbers), len(version2_numbers))

    def get_version_by_index(numbers, index: int):
        try:
            return int(numbers[index])
        except:
            return 0

    for i in range(max_range):
        version1_index = get_version_by_index(version1_numbers, i)
        version2_index = get_version_by_index(version2_numbers, i)
        if version1_index > version2_index:
            return 1
        elif version1_index < version2_index:
            return -1
    return 0


json_fixture = [
    {
        "id": "a84f6978-3c7c-4b48-9016-08f655bd8361",
        "content": "co",
        "createdDate": "2011-10-05T14:48:00.000Z",
        "modifiedDate": "2011-10-05T14:48:00.000Z",
        "tags": "TAG1,TAG2",
        "title": "ti",
        "type": "is a string representing an item type",
        "dueDate": "2011-10-05T14:48:00.000Z"
    },
    {
        "id": "a84f6978-3c7c-4b48-9016-08f655bd8361",
        "content": "content 1",
        "createdDate": "2011-09-05T14:48:00.000Z",
        "modifiedDate": "2011-09-05T14:48:00.000Z",
        "tags": "TAG1,TAG2",
        "title": "title 1",
        "type": "is a string representing an item type",
        "dueDate": "2011-10-05T14:48:00.000Z"
    },
    {
        "id": "a84f6978-3c7c-4b48-9016-08f655bd8361",
        "content": "text 1",
        "createdDate": "2011-11-05T14:48:00.000Z",
        "modifiedDate": "2011-11-05T14:48:00.000Z",
        "tags": "TAG1,TAG2",
        "title": "title 1",
        "type": "is a string representing an item type",
        "dueDate": "2011-10-05T14:48:00.000Z"
    },
]


def find_items_by_string(items, string: str):
    if len(string) < 3:
        return items

    def check_string(item):
        attributes = ['content', 'title']
        valid = False
        for attr in attributes:
            if string in item.get(attr):
                valid = True
        return valid

    return list(filter(check_string, items))


def sort_items_by_field(items, direction: str, field: str):
    items_copy = items.copy()

    reverse = True if direction == 'desc' else False
    items_copy.sort(reverse=reverse, key=lambda x: x.get(field))

    return items_copy


def add_tag_items_by_string(items, string: str):
    searched_items = find_items_by_string(items, string)

    def add_tag(item):
        ARCHIVED_TAG = 'ARCHIVED'
        tags = item.get('tags').split(',')
        if ARCHIVED_TAG not in tags:
            tags.append(ARCHIVED_TAG)
        item['tags'] = ','.join(tags)
        return item

    searched_items = list(map(add_tag, searched_items))
    return sort_items_by_field(searched_items, 'asc', 'createdDate')


print(find_items_by_string(json_fixture, 'title'))
print(find_items_by_string(json_fixture, 'con'))
print(find_items_by_string(json_fixture, 'co'))
print(sort_items_by_field(json_fixture, 'asc', 'createdDate'))
print(sort_items_by_field(json_fixture, 'desc', 'createdDate'))
print(sort_items_by_field(json_fixture, 'asc', 'modifiedDate'))
print(sort_items_by_field(json_fixture, 'desc', 'modifiedDate'))
print(add_tag_items_by_string(json_fixture, 'title1'))
