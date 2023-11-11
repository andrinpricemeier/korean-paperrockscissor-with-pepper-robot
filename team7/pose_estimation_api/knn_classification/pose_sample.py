class PoseSample(object):
  """Sample in our training set based on manually assigning a class to each set of landmark coordinates."""
  def __init__(self, name, landmarks, class_name, embedding):
    self.name = name
    self.landmarks = landmarks
    self.class_name = class_name    
    self.embedding = embedding