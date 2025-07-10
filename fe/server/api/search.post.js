export default defineEventHandler(async (event) => {
  const body = await readBody(event);
  const query = body.query || '';

  // Simulated mock response
  return [
    {
      video_id: 'vid001',
      video_url: '/sample/accident.mp4',
      confidence: 'High',
      start: 0,
      end: 90,
      score: 0.93
    }
  ];
});
