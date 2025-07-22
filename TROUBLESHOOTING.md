# 🔧 Troubleshooting Guide

This guide helps you resolve common issues with the Automated Customer Support Chatbot.

## 🚨 Common Issues and Solutions

### 1. **OpenAI API Key Issues**

**Problem**: "I'm having trouble with my authentication" or "I'm not properly configured"

**Solutions**:
- Create a `.env` file in the project root
- Add your OpenAI API key: `OPENAI_API_KEY=your_actual_api_key_here`
- Get an API key from [OpenAI Platform](https://platform.openai.com/api-keys)
- Make sure you have credits in your OpenAI account

### 2. **Rasa Action Server Not Starting**

**Problem**: "Action server not found" or connection errors

**Solutions**:
```bash
# Start the action server
rasa run actions

# In a separate terminal, start Rasa server
rasa run --enable-api
```

### 3. **Model Training Issues**

**Problem**: Training fails or model doesn't work properly

**Solutions**:
```bash
# Clean and retrain
rasa train --force

# Check for syntax errors
rasa data validate

# Test the model
rasa test
```

### 4. **Dependency Conflicts**

**Problem**: Import errors or version conflicts

**Solutions**:
```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# If issues persist, try updating
pip install --upgrade rasa openai
```

### 5. **Streamlit App Not Connecting to Rasa**

**Problem**: "Error: 500" or connection refused

**Solutions**:
- Ensure Rasa server is running on port 5005
- Check if action server is running on port 5055
- Verify `endpoints.yml` configuration
- Check firewall settings

### 6. **Intent Recognition Issues**

**Problem**: Bot doesn't understand user queries

**Solutions**:
- Add more training examples to `data/nlu.yml`
- Retrain the model: `rasa train`
- Check intent confidence scores: `rasa shell`
- Review entity extraction in domain.yml

### 7. **Memory Issues**

**Problem**: High memory usage or crashes

**Solutions**:
- Reduce model complexity in `config.yml`
- Lower epochs in training configuration
- Use smaller models (gpt-3.5-turbo instead of gpt-4)
- Monitor system resources

## 🔍 Debugging Steps

### Step 1: Check Environment
```bash
python setup.py
```

### Step 2: Validate Configuration
```bash
rasa data validate
```

### Step 3: Test Components
```bash
# Test NLU
rasa shell nlu

# Test dialogue
rasa shell

# Test actions
rasa run actions
```

### Step 4: Check Logs
```bash
# Enable debug logging
rasa run --enable-api --debug

# Check action server logs
rasa run actions --debug
```

## 📊 Performance Optimization

### 1. **Reduce Training Time**
- Lower epochs in `config.yml`
- Use smaller training datasets
- Enable caching: `rasa train --cache`

### 2. **Improve Response Time**
- Use faster models (gpt-3.5-turbo)
- Implement response caching
- Optimize action server performance

### 3. **Memory Optimization**
- Use smaller models
- Implement conversation cleanup
- Monitor memory usage

## 🛠️ Advanced Troubleshooting

### Custom Action Issues
If custom actions aren't working:
1. Check action server is running
2. Verify action names in `domain.yml`
3. Check action server logs
4. Ensure proper imports in `actions/actions.py`

### Entity Extraction Issues
If entities aren't being extracted:
1. Add more entity examples in training data
2. Check entity synonyms
3. Verify entity mappings in `domain.yml`
4. Retrain the model

### Conversation Flow Issues
If conversations aren't flowing correctly:
1. Check `stories.yml` for proper flows
2. Verify `rules.yml` configuration
3. Test conversation paths
4. Review slot mappings

## 📞 Getting Help

If you're still experiencing issues:

1. **Check the logs** for specific error messages
2. **Search existing issues** in the repository
3. **Create a new issue** with:
   - Error message
   - Steps to reproduce
   - Environment details
   - Log files

## 🔄 Quick Reset

If everything is broken, try this complete reset:

```bash
# Remove old models and cache
rm -rf models/*.tar.gz
rm -rf .rasa/

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall

# Retrain model
rasa train

# Start fresh
rasa run actions &
rasa run --enable-api &
streamlit run app.py
```

## 📝 Log Locations

- **Rasa logs**: `~/.rasa/logs/`
- **Action server logs**: Console output
- **Streamlit logs**: Console output
- **OpenAI errors**: Check API dashboard

---

**Remember**: Most issues can be resolved by checking the logs and ensuring all services are running properly! 