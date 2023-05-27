from app import app
import multiprocessing

workers = (multiprocessing.cpu_count()) * 2 + 1
threads = workers
if __name__ == '__main__':
    app.run(debug=true)
