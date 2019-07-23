
# chunked file reading
from __future__ import division
import os

to_file='chunk.log'

def get_chunks(file_size):
    chunk_start = 0
    chunk_size = 1024*1024  # 131072 bytes, default max ssl buffer size
    while chunk_start + chunk_size < file_size:
        yield(chunk_start, chunk_size)
        chunk_start += chunk_size

    final_chunk_size = file_size - chunk_start
    yield(chunk_start, final_chunk_size)

def read_file_chunked(file_path):
    with open(file_path, 'rb') as file_:
        file_size = os.path.getsize(file_path)

        for chunk_start, chunk_size in get_chunks(file_size):
            file_chunk = file_.read(chunk_size)
            file_chunk = file_chunk.decode('UTF-8', 'ignore').strip().strip(b'\x00'.decode())
            with open(to_file, 'a') as f:
                f.write(file_chunk)    

if __name__ == '__main__':
    read_file_chunked('temp.log')
