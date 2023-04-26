import os



def delete():
    path = 'C:\\Users\\Shreyank M\\PycharmProjects\\pythonProject2\\allurereportsdemo\\report'
    for filename in os.listdir(path):
        if filename.endswith('.png') or filename.endswith('.json') or filename.endswith('.jpg'):
            os.remove(os.path.join(path, filename))

# def test_something():
#     # Your test case code goes here
#     pass

