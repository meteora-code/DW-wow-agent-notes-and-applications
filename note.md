# zigent_instructor.ipynb
实现了一个教程生成助手，通过 WriteContent 和 TutorialAssistant 两个类来生成教程内容，可以根据主题自动生成目录结构和详细内容，支持多语言输出，自动保存为markdown格式
# zigent_philosophy.ipynb
实现了一个哲学讨论系统，创建了三个哲学家角色(孔子、苏格拉底、亚里士多德)，通过 ManagerAgent 来协调三个哲学家进行讨论，可以针对问题获取三位哲学家的不同观点和总结
# zigent_search.ipynb
实现了两种搜索功能(DuckDuckGo和智谱)，通过 DuckSearchAction 和 ZhipuSearchAction 来执行搜索，可以获取在线内容并整合到回答中，智谱搜索相比DuckDuckGo效果更好
# zigent_story.ipynb
实现了一个故事生成助手，通过 StoryAssistant 类来生成故事内容，可以根据主题自动生成目录结构和详细内容，支持多语言输出，自动保存为markdown格式
## 改进
- 在aigent源码中添加流式输出功能
- 改动提示词，指导AI创作小说
