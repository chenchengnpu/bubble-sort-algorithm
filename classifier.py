"""
简单分类识别器
使用 scikit-learn 实现文本分类
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import numpy as np


# 训练数据
documents = [
    "这是一篇关于体育的文章",
    "足球比赛非常精彩",
    "篮球队赢得了冠军",
    "运动员们在赛场上拼搏",
    "这是一篇关于科技的文章",
    "人工智能发展迅速",
    "智能手机功能强大",
    "新技术改变我们的生活",
    "这是一篇关于娱乐的文章",
    "明星的新闻总是受到关注",
    "电影票房创新高",
    "音乐会门票售罄",
    "这是一篇关于美食的文章",
    "餐厅的菜品很美味",
    "烹饪技巧很重要",
    "美食节吸引大量游客"
]

# 标签
labels = [
    "体育", "体育", "体育", "体育",
    "科技", "科技", "科技", "科技",
    "娱乐", "娱乐", "娱乐", "娱乐",
    "美食", "美食", "美食", "美食"
]


def train_classifier():
    """训练分类器"""
    # 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(
        documents, labels, test_size=0.25, random_state=42
    )
    
    # TF-IDF 向量化
    vectorizer = TfidfVectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    
    # 训练朴素贝叶斯分类器
    clf = MultinomialNB()
    clf.fit(X_train_vec, y_train)
    
    # 预测
    y_pred = clf.predict(X_test_vec)
    
    # 输出结果
    print("=" * 50)
    print("分类识别器训练完成!")
    print("=" * 50)
    print(f"\n准确率: {accuracy_score(y_test, y_pred):.2%}")
    print("\n分类报告:")
    print(classification_report(y_test, y_pred))
    
    return vectorizer, clf


def predict(vectorizer, clf, text):
    """预测文本类别"""
    text_vec = vectorizer.transform([text])
    prediction = clf.predict(text_vec)[0]
    probabilities = clf.predict_proba(text_vec)[0]
    
    return prediction, dict(zip(clf.classes_, probabilities))


if __name__ == "__main__":
    # 训练分类器
    vectorizer, clf = train_classifier()
    
    # 测试预测
    test_texts = [
        "球队获得了胜利",
        "最新款手机发布了",
        "明星参加了颁奖典礼",
        "这道菜非常好吃"
    ]
    
    print("\n" + "=" * 50)
    print("测试预测结果:")
    print("=" * 50)
    
    for text in test_texts:
        pred, prob = predict(vectorizer, clf, text)
        print(f"\n文本: {text}")
        print(f"预测类别: {pred}")
        print(f"概率: {prob[pred]:.2%}")
