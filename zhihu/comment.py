#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Comment:

    """评论类，请使用``ZhihuClient.Comment``方法构造对象."""

    def __init__(self, id, answer, author,
                 upvote_num, content, group_id=None):
        """创建评论类实例.

        :param int id: 评论ID
        :param int group_id: 评论所在的组ID
        :param Answer answer: 评论所在的答案对象
        :param Author author: 评价的作者对象
        :param int upvote_num: 评价赞同数量
        :param str content: 评价内容
        :return: 评价对象
        :rtype: Comment
        """

        self.id = id
        self.answer = answer
        self.author = author
        self.upvote_num = upvote_num
        self.content = content
        self._group_id = group_id
