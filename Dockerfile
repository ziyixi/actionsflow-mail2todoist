From nikolaik/python-nodejs:python3.7-nodejs14-slim
RUN pip install todoist-python \
    && pip install markdownify
COPY post_task.py /github/workspace/post_task.py