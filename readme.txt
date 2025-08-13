# AI-Roaster 🔥

> An AI-powered bot that dishes out spicy roasts, sweet compliments, and neutral zingers. Built with NLP and developer humor, it's here to hype you up, make you laugh, or roast you into better code.

Made with ❤️ by **Fahmida Fathima the Savage Fierce** 👸

## 🎯 What is AI-Roaster?

AI-Roaster is your personal AI comedian that can:
- 🌶️ **Roast you** with savage (but funny) burns
- 💖 **Compliment you** with genuine praise and encouragement  
- 😐 **Stay neutral** with witty but balanced zingers
- 💻 **Understand developer life** with programming humor and references

Whether you need motivation, a good laugh, or just want to see if an AI can out-sass you, AI-Roaster has got your back!

## ✨ Features

- **Multiple Personality Modes**: Choose between roasting, complimenting, or neutral responses
- **Developer-Focused Humor**: Understands coding struggles, debugging nightmares, and tech culture
- **Natural Language Processing**: Powered by AI to generate contextual and relevant responses
- **Customizable Intensity**: From gentle teasing to savage roasts (all in good fun!)
- **Interactive Experience**: Engaging conversation flow that adapts to your inputs

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/FahmidaFathima/AI-Roaster.git
   cd AI-Roaster
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

## 🎮 Usage

### Basic Commands

```python
# Initialize the roaster
from ai_roaster import AIRoaster

roaster = AIRoaster()

# Get a roast
roaster.roast("I think I'm a great programmer")

# Get a compliment
roaster.compliment("I just fixed a bug after 3 hours")

# Get a neutral zinger
roaster.neutral("I use vim btw")
```

### Command Line Interface

```bash
# Interactive mode
python ai_roaster.py --interactive

# Single roast
python ai_roaster.py --roast "Your message here"

# Compliment mode
python ai_roaster.py --compliment "Your achievement here"
```

## 🛠️ Configuration

Create a `.env` file in the project root:

```env
# AI Model Configuration
OPENAI_API_KEY=your_api_key_here
MODEL_NAME=gpt-3.5-turbo

# Roaster Settings
DEFAULT_MODE=roast
INTENSITY_LEVEL=medium
DEVELOPER_FOCUSED=true
```

## 📝 Examples

### Roast Mode 🔥
```
Input: "I only code in Python because it's easy"
Output: "Oh, so you're the person who thinks using training wheels makes you a motorcyclist? Python is great, but calling yourself a programmer because you can import libraries is like calling yourself a chef because you can microwave frozen dinners! 🔥"
```

### Compliment Mode 💖
```
Input: "I just deployed my first app to production"
Output: "Look at you conquering the digital world! 🚀 From localhost to the real world - that's not just code deployment, that's dreams deployment! Your first production app is like your first steps, except this time the whole internet can see you walk. Absolutely legendary! 💖"
```

### Neutral Mode 😐
```
Input: "I've been debugging this for 6 hours"
Output: "Ah yes, the ancient ritual of staring at code until either you break it or it breaks you. Six hours means you're either very thorough or very stubborn. Probably both. The bug is probably a missing semicolon, isn't it? 😐"
```

## 🧠 How It Works

AI-Roaster uses advanced Natural Language Processing to:

1. **Analyze Input Context**: Understands the sentiment and topic of your message
2. **Select Response Mode**: Determines whether to roast, compliment, or stay neutral
3. **Generate Contextual Response**: Creates relevant, humorous responses using AI
4. **Apply Developer Flavor**: Adds programming references and tech culture jokes
5. **Deliver with Style**: Formats responses with emojis and personality

## 🤝 Contributing

Want to make AI-Roaster even more savage? Contributions welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/savage-improvement`)
3. Commit your changes (`git commit -am 'Add more roasting power'`)
4. Push to the branch (`git push origin feature/savage-improvement`)
5. Create a Pull Request

### Contributing Guidelines

- Keep the humor light and inclusive
- Test your roasts on yourself first
- Add appropriate documentation
- Follow the existing code style
- Include examples for new features

## 📋 Roadmap

- [ ] **Web Interface**: Browser-based roasting experience
- [ ] **Discord Bot Integration**: Bring the roasts to your server
- [ ] **Slack Integration**: Roast your coworkers (professionally)
- [ ] **Custom Training**: Train on your own humor style
- [ ] **Roast Templates**: Predefined roast categories
- [ ] **Multi-language Support**: Roasts in different languages
- [ ] **Voice Mode**: Audio roasts and compliments

## 🐛 Known Issues

- Sometimes roasts are too good and hurt feelings (working on sensitivity settings)
- May occasionally compliment your code TOO much
- Neutral mode might be funnier than roast mode

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👸 About the Author

**Fahmida Fathima the Savage Fierce** - A developer who believes humor makes coding better, roasts make you stronger, and compliments make the world go round.

- GitHub: [@FahmidaFathima](https://github.com/FahmidaFathima)
-Linkedin 
https://www.linkedin.com/in/fahmida-fathima-ai/ 

## 🙏 Acknowledgments

- OpenAI for making AI roasting possible
- The developer community for being such good sports
- Coffee, for fueling the late-night coding sessions that inspired this
- Everyone who's ever been roasted by their own code


## ⚠️ Disclaimer

AI-Roaster is designed for entertainment and motivation. All roasts are meant in good fun. If you're easily offended, maybe stick to compliment mode! 😉

**Remember**: Good code speaks for itself, but great developers can laugh at themselves! 🚀

