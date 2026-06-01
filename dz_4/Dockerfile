# syntax=docker/dockerfile:1

# --- Stage 1: install production dependencies (cached layer) ---
FROM node:22-alpine AS deps

WORKDIR /app

COPY package.json ./

RUN npm install --omit=dev && npm cache clean --force

# --- Stage 2: minimal runtime image ---
FROM node:22-alpine AS runner

WORKDIR /app

ENV NODE_ENV=production \
    PORT=3000 \
    HOST=0.0.0.0

RUN addgroup -g 1001 -S app && adduser -S app -u 1001 -G app

COPY --from=deps /app/node_modules ./node_modules
COPY package.json server.js ./
COPY public ./public

USER app

EXPOSE 3000

CMD ["node", "server.js"]
