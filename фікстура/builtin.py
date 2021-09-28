# Если вы тестируете что-то, что считывает, записывает или изменяет файлы,
# вы можете использовать tmpdir для создания файлов или каталогов, используемых одним тестом,
# и вы можете использовать tmpdir_factory, когда хотите настроить каталог для нескольких тестов.

# Фикстура tmpdir имеет область действия функции (function scope),
# и фикстура tmpdir_factory имеет область действия сеанса (session scope).
import json
import pytest


def test_tmpdir(tmpdir):
    # tmpdir уже имеет имя пути, связанное с ним
    # join() расширяет путь, чтобы включить имя файла,
    # создаваемого при записи в
    a_file = tmpdir.join('something.txt')

    # можете создавать каталоги
    a_sub_dir = tmpdir.mkdir('anything')

    # можете создавать файлы в директориях (создаются при записи)
    another_file = a_sub_dir.join('something_else.txt')

    # эта запись создает 'something.txt'
    a_file.write('contents may settle during shipping')

    # эта запись создает 'anything/something_else.txt'
    another_file.write('something different')

    # вы также можете прочитать файлы
    assert a_file.read() == 'contents may settle during shipping'
    assert another_file.read() == 'something different'


def test_tmpdir_factory(tmpdir_factory):
    # вы должны начать с создания каталога. a_dir действует как
    # объект, возвращенный из фикстуры tmpdir
    a_dir = tmpdir_factory.mktemp('mydir')

    # base_temp будет родительским каталогом 'mydir' вам не нужно
    # использовать getbasetemp(), чтобы
    # показать, что он доступен
    base_temp = tmpdir_factory.getbasetemp()
    print('base:', base_temp)

    # остальная часть этого теста выглядит так же,
    # как в Примере ' test_tmpdir ()', за исключением того,
    # что я использую a_dir вместо tmpdir

    a_file = a_dir.join('something.txt')
    a_sub_dir = a_dir.mkdir('anything')
    another_file = a_sub_dir.join('something_else.txt')

    a_file.write('contents may settle during shipping')
    another_file.write('something different')

    assert a_file.read() == 'contents may settle during shipping'
    assert another_file.read() == 'something different'


@pytest.fixture(scope='module')
def author_file_json(tmpdir_factory):
    """Пишем некоторых авторов в файл данных."""
    python_author_data = {
        'Ned': {'City': 'Boston'},
        'Brian': {'City': 'Portland'},
        'Luciano': {'City': 'Sau Paulo'}
    }

    file = tmpdir_factory.mktemp('data').join('author_file.json')
    print('file:{}'.format(str(file)))

    with file.open('w') as f:
        json.dump(python_author_data, f)
    return file


def test_brian_in_portland(author_file_json):
    """Тест, использующий файл данных."""
    with author_file_json.open() as f:
        authors = json.load(f)
    assert authors['Brian']['City'] == 'Portland'


def test_all_have_cities(author_file_json):
    """Для обоих тестов используется один и тот же файл."""
    with author_file_json.open() as f:
        authors = json.load(f)
    for a in authors:
        assert len(authors[a]['City']) > 0